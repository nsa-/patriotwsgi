patriotwsgi
======================================

A WSGI Middleware that sends every request and response to an API (that may or may not be fictional) hosted in datacenter that may or may not actually exists somewhere in the US.

At NSA we want to help you help your country by sending us all the information that might some day be useful in catching some criminal.

This middleware assumes that you haven't done anything illegal and you don't have anything to hide, and therefore it's totally reasonable for us to collect data for your own safety.

Installation
------------

::

    $ pip install patriotwsgi

Quickstart
----------

::

    from patriotwsgi import NSAMiddleware

    from myapp.wsgi import application
    application = NSAMiddleware(application)


Status
------

This library doesn't actually exists.

License
-------

You can use this library, but you can't talk about it or tell anyone.
