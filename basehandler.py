# *-* coding: UTF-8 *-*

# shortened version of https://raw.github.com/coto/gae-boilerplate/master/boilerplate/lib/basehandler.py

# standard library imports
import logging
# related third party imports
import webapp2
from webapp2_extras import jinja2
from webapp2_extras import sessions
# local application/library specific imports
import models
from google.appengine.api import users
import socket
from urlparse import urlparse
from datetime import datetime
from datetime import timedelta
import pytz
from config import config
import string
import random
#import base64
import os
import math
import sys


def random_string(size=32, chars=string.ascii_letters + string.digits):
    """ Generate random string """
    return os.urandom(32).encode('hex')


def generate_csrf_token():
    session = sessions.get_store().get_session()
    if '_csrf_token' not in session:
        session['_csrf_token'] = random_string()
    return session['_csrf_token']


def jinja2_factory(app):
    j = jinja2.Jinja2(app)
    j.environment.filters.update({
        # Set filters.
        # ...
    })
    j.environment.globals.update({
        # Set global variables.
        'csrf_token': generate_csrf_token,
        'uri_for': webapp2.uri_for,
        'getattr': getattr,
        'session': BaseHandler.session,
    })
    j.environment.tests.update({
        # Set test.
        # ...
    })
    return j


class ViewClass:
    """
        ViewClass to insert variables into the template.

        ViewClass is used in BaseHandler to promote variables automatically that can be used
        in jinja2 templates.
        Use case in a BaseHandler Class:
            self.view.var1 = "hello"
            self.view.array = [1, 2, 3]
            self.view.dict = dict(a="abc", b="bcd")
        Can be accessed in the template by just using the variables like {{var1}} or {{dict.b}}
    """
    pass


class BaseHandler(webapp2.RequestHandler):
    """
        BaseHandler for all requests

        Holds the auth and session properties so they
        are reachable for all requests
    """

    def __init__(self, request, response):
        """ Override the initialiser in order to set the language.
        """
        self.initialize(request, response)
        self.view = ViewClass()

    def dispatch(self):
        """
            Get a session store for this request.
        """
        self.session_store = sessions.get_store(request=self.request)

        try:
            # csrf protection
            if self.request.method == "POST":
                token = self.session.get('_csrf_token')
                if not token or token != self.request.get('_csrf_token'):
                    self.abort(403)

            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session_store(self):
        return sessions.get_store(request=self.request)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

    @webapp2.cached_property
    def auth_config(self):
        """ Dict to hold urls for login/logout """
        return {
            'login_url': users.create_login_url('/login-return'),
            'logout_url': users.create_logout_url('/')
        }

    @webapp2.cached_property
    def user(self):
        return users.get_current_user()

    @webapp2.cached_property
    def user_id(self):
        return str(self.user.user_id()) if self.user else None

    @webapp2.cached_property
    def email(self):
        return self.user.email() if self.user else None

    @webapp2.cached_property
    def nickname(self):
        return self.user.nickname() if self.user else None

    @webapp2.cached_property
    def is_user_admin(self):
        return users.is_current_user_admin()

    @webapp2.cached_property
    def messages(self):
        return self.session.get_flashes(key='_messages')

    def add_message(self, message, level=None):
        self.session.add_flash(message, level, key='_messages')

    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(factory=jinja2_factory, app=self.app)

    def render_template(self, filename, **kwargs):

        referer = self.request.referer
        referer_domain = None
        if referer != None:
            parsed_uri = urlparse(referer)
            referer_domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

        # make all self.view variables available in jinja2 templates
        if hasattr(self, 'view'):
            kwargs.update(self.view.__dict__)

        if self.request.get('theme') != None and self.request.get('theme') != '':
            #logging.info('setting session.theme:%s' % self.request.get('theme'))
            self.session['theme'] = self.request.get('theme')

        # set or overwrite special vars for jinja templates
        kwargs.update({
            'user': self.user,
            #'user_id': self.user_id,
            #'email': self.email,
            #'nickname': self.nickname,
            'is_user_admin': self.is_user_admin,
            #'now': (datetime.utcnow() + timedelta(hours=+1)),#offset for dublin
            'now': datetime.now(pytz.timezone('US/Eastern')),
            'url': self.request.url,
            'path': self.request.path,
            'query_string': self.request.query_string,
            'session': self.session,
            'referer': referer,# None or refereing URL
            'referer_domain': referer_domain,
            'server': socket.getfqdn(),
            'themes': config['themes'],
            'tags': config['tags'],
        })
        kwargs.update(self.auth_config)
        if self.messages:
            kwargs['messages'] = self.messages

        self.response.headers.add_header('X-UA-Compatible', 'IE=Edge,chrome=1')
        try:
            self.response.write(self.jinja2.render_template(filename, **kwargs))
        except:
            logging.warning(sys.exc_info())
            self.abort(404)