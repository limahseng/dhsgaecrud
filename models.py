#Data model

from google.appengine.ext import ndb

class EmployeeModel (ndb.Model):
	name = ndb.StringProperty()
	gender = ndb.StringProperty()
	dob = ndb.DateProperty()
	email = ndb.StringProperty()
	timestamp = ndb.DateTimeProperty(auto_now=True)