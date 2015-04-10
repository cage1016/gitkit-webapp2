#!/usr/bin/env python

import webapp2
from controllers.base import BaseRequestHandler

# Import the helper functions
from identitytoolkit import gitkitclient

# Import the configuration file you downloaded from Google Developer Console
gitkit_instance = gitkitclient.GitkitClient.FromConfigFile('gitkit-server-config.json')

class MainHandler(BaseRequestHandler):
  def get(self):

    params = dict(text='You are not signed in.')

    # Check for and read the Google Identity Toolkit token if present

    if 'gtoken' in self.request.cookies:
      gitkit_user = gitkit_instance.VerifyGitkitToken(self.request.cookies['gtoken'])
      if gitkit_user:
        params['text'] = "Welcome " + gitkit_user.email + "! Your user info is: " + str(vars(gitkit_user))

    self.render('index.html', **params)


class WidgetHandler(BaseRequestHandler):
  def get(self):
    self.render('widget.html')


routes = [
  ('/', MainHandler),
  ('/widget', WidgetHandler)
]

router = webapp2.WSGIApplication(routes, debug=True)