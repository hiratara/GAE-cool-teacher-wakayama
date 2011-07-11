# -*- coding: utf-8 -*-
import oauth
import random
import yaml
import codecs

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch

class MainPage(webapp.RequestHandler):
    def __init__(self):
        fh = codecs.open("config.yaml", "r", "UTF-8")
        self.config = yaml.load(fh)

    def a_dajare(self):
        return random.choice(self.config["gags"])

    def get(self):
        client = oauth.TwitterClient(
            self.config["application_key"],
            self.config["application_secret"],
            "")

        url = "http://twitter.com/statuses/update.xml"
        result = client.make_request(
            url=url, additional_params={"status":self.a_dajare()},
            token=self.config["user_token"], 
            secret=self.config["user_secret"], 
            method=urlfetch.POST)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(result.content)

application = webapp.WSGIApplication(
    [('/jobs', MainPage)],
    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
