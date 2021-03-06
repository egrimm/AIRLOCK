# *-* coding: UTF-8 *-*
#-------------------------------------------------------------------------------
# Name:        handlers
# Purpose:     most site handlers
#
# Author:      Eric
#
# Created:     2016-02-26
# Copyright:   (c) Eric 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from basehandler import BaseHandler
from decorators import user_required, admin_required
import os
from config import config

#import logging
#import sys
#import webapp2
#from google.appengine.api import users # we are using this for authentication
#from google.appengine.ext import ndb
#import models # we are using this for authorization and storing of further pii
#import re
#import datetime

DEV = os.environ['SERVER_SOFTWARE'].startswith('Development')


def generate_auth_token(key, url, ts, contest_id, student_id=''):
    from hashlib import sha1
    import hmac

    msg = url + str(ts) + str(contest_id) + str(student_id)
    hashed = hmac.new(key, msg, sha1)
    auth_token = hashed.hexdigest()
    return auth_token


class UpdateHandler(BaseHandler):
    # all updates go here
    
    @admin_required
    def get(self):
        import urllib2
        import json
           
        self.response.out.write('<html><body>')
        
        self.response.out.write('<h1>running updates</h1>')
        # todo: implement
        self.response.out.write('<h2>updates finished.</h2>')
        self.response.out.write('<p><a href="/">Home</a></p>')

        self.response.out.write('</body></html>')


## STATIC TEMPLATE HANDLERS ##
class MainHandler(BaseHandler):
    def get(self):
        params = {}
        return self.render_template('home.html', **params)


class AboutHandler(BaseHandler):
    def get(self, club=None):
        params = {}
        if club == None:
            return self.render_template('about.html', **params)
        params['links'] = config['club_links'][club]
        return self.render_template('about-'+club+'.html', **params)


class RecipeHandler(BaseHandler):
    def get(self, style=None, name=None):
        params = {}
        if style == None:
            return self.render_template('recipes.html', **params)
        elif style != None and name == None:
            # todo: get <style> recipes to display in list or table
            return self.render_template('recipes-'+style+'.html', **params)
        elif style != None and name != None:
            # todo: get <name> recipe to display
            return self.render_template('recipes-'+style+'-'+name+'.html', **params)

    def post(self):
        params = {}
        message = 'Search functionality is coming soon!'
        self.add_message(message, 'info')
        return self.render_template('recipes.html', **params)


class NewsHandler(BaseHandler):
    def get(self):
        params = {}
        return self.render_template('news.html', **params)


class EventsHandler(BaseHandler):
    def get(self):
        params = {}
        return self.render_template('events.html', **params)


class ResourcesHandler(BaseHandler):
    def get(self):
        params = {}
        return self.render_template('resources.html', **params)


