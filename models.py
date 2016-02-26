from google.appengine.api import memcache
from google.appengine.ext import ndb
from google.appengine.datastore.datastore_query import Cursor
import logging

# note if you change the schema, the following article may be useful:
#
# https://developers.google.com/appengine/articles/update_schema?csw=1
#
# describes a method of updating entities that may not have any new properties
# you add to the model, which may cause them to become un-queryable


