from google.appengine.ext import ndb
import webapp2
import json
import logging

class OauthHandler(webapp2.RequestHandler):
	def get(self):
	    self.response.write("bye")
		
class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write("hello")


app = webapp2.WSGIApplication([
    ('/', MainPage), 
	('/oauth', OauthHandler)
	
], debug=True)
