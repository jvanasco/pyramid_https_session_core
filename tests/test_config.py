from __future__ import print_function

# stdlib
import unittest

# pyramid testing requirements
from pyramid import testing
from pyramid.config import Configurator
from pyramid.exceptions import ConfigurationError
from pyramid.response import Response
from pyramid.request import Request
from pyramid.session import SignedCookieSessionFactory

# local
import pyramid_https_session_core


# ------------------------------------------------------------------------------


def view_cookie_unused(request):
    return Response(
        "<html><head></head><body>OK</body></html>", content_type="text/html"
    )


def view_cookie_used(request):
    request.session_https["foo"] = "bar"
    return Response(
        "<html><head></head><body>OK</body></html>", content_type="text/html"
    )


class TestCookieUnused(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.settings = self.config.registry.settings
        my_session_factory = SignedCookieSessionFactory("itsaseekreet")
        pyramid_https_session_core.register_https_session_factory(
            self.config, self.settings, my_session_factory
        )
        # create a view
        self.config.add_view(view_cookie_unused)

    def tearDown(self):
        testing.tearDown()

    def test_itworked(self):

        # make the app
        app = self.config.make_wsgi_app()

        # make a request
        req1 = Request.blank("/")
        req1.remote_addr = "127.0.0.1"
        resp1 = req1.get_response(app)
        self.assertEqual(resp1.status_code, 200)
        self.assertNotIn("Set-Cookie", resp1.headers)


class TestCookieUsed(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.settings = self.config.registry.settings
        my_session_factory = SignedCookieSessionFactory("itsaseekreet")
        pyramid_https_session_core.register_https_session_factory(
            self.config, self.settings, my_session_factory
        )
        # create a view
        self.config.add_view(view_cookie_used)

    def tearDown(self):
        testing.tearDown()

    def test_itworked(self):

        # make the app
        app = self.config.make_wsgi_app()

        # make a request
        req1 = Request.blank("/")
        req1.remote_addr = "127.0.0.1"
        resp1 = req1.get_response(app)
        self.assertEqual(resp1.status_code, 200)
        self.assertIn("Set-Cookie", resp1.headers)
