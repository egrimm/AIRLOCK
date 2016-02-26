#-------------------------------------------------------------------------------
# Name:        decorators
# Purpose:
#
# Author:      egrimm
#
# Created:     2016-02-26
# Copyright:   (c) egrimm 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from basehandler import BaseHandler
from config import config
from google.appengine.api import users
from urlparse import urlparse
import logging
import socket
    


def admin_required(handler):
    def check_session(self, *args, **kwargs):
        #logging.info('users.is_current_user_admin(): %s' % users.is_current_user_admin())
        if users.get_current_user() is None:
            self.redirect(self.uri_for('home'), abort=True)
        elif users.is_current_user_admin() == False:
            self.redirect(self.uri_for('home'), abort=True)
        return handler(self, *args, **kwargs)
    return check_session


def user_required(handler):
    def check_session(self, *args, **kwargs):
        if users.get_current_user() is None:
            self.redirect(login_url, abort=True)
        return handler(self, *args, **kwargs)
    return check_session


def same_domain_required(handler):
    def check_referer(self, *args, **kwargs):
        if self.request.referer is None:
            self.redirect(self.uri_for('home'), abort=True)
        else:
            # check referer host against server domain
            parsed_uri = urlparse(self.request.referer)
            referer_domain = '{uri.netloc}'.format(uri=parsed_uri)
            if referer_domain != socket.getfqdn():
                self.redirect(self.uri_for('home'), abort=True)
        return handler(self, *args, **kwargs)
    return check_referer