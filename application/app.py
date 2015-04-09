#!/usr/bin/env python

import webapp2
from controllers.base import BaseRequestHandler


class MainHandler(BaseRequestHandler):
  def get(self):
    self.render('index.html')


routes = [
  ('/', MainHandler)
]

router = webapp2.WSGIApplication(routes, debug=True)