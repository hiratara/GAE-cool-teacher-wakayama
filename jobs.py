# -*- coding: utf-8 -*-
import oauth
import random
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch

dajare = [
# だじゃれ設定
]

def a_dajare():
    return random.choice(dajare)

class MainPage(webapp.RequestHandler):
    def get(self):
        application_key = ""
        application_secret = ""
        user_token = ""
        user_secret = ""

        client = oauth.TwitterClient(
            application_key, application_secret, 
            "")

        url = "http://twitter.com/statuses/update.xml"
        result = client.make_request(
            url=url, additional_params={"status":a_dajare()},
            token=user_token, secret=user_secret, method=urlfetch.POST)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(result.content)

application = webapp.WSGIApplication(
    [('/jobs', MainPage)],
    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
