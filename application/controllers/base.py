# -*- encoding: utf-8 -*-

import webapp2
from webapp2_extras import auth, sessions, jinja2
from jinja2.runtime import TemplateNotFound


class BaseRequestHandler(webapp2.RequestHandler):
  @webapp2.cached_property
  def jinja2(self):
    """Returns a Jinja2 renderer cached in the app registry"""

    j = jinja2.get_jinja2(app=self.app)
    # j.environment.filters['date'] = jinja2_date_filter
    # j.environment.filters['soical_media_icon'] = soical_media_icon_filter
    return j

  def render(self, template_name, **template_vars):
    # Preset values for the template
    values = {}

    # read the template or 404.html
    try:
      self.response.write(self.jinja2.render_template(template_name, **values))
    except TemplateNotFound:
      self.abort(404)

