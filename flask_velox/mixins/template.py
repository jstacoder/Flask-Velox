# -*- coding: utf-8 -*-

"""
Module provides mixins for rendering templates using Flask `MethodView`.

Example
-------

>>> from flask import Flask
... from flask.ext.velox.mixins.template import TemplateMixin
... from flask.views import MethodView
...
... app = Flask(__name__)
...
... class MyView(TemplateMixin):
...     template = 'templates/home.html'
...
... app.add_url_rule('/', view_func=MyView.as_view('myview'))
...
... app.run()

"""

from flask import render_template
from flask.views import MethodView


class TemplateMixin(MethodView):
    """ Renders a template on HTTP GET request as long as the ``template``
    attribute is defined.

    Attributes
    ----------
    template : str
        Relative template path, e.g: ``templates/home.html``

    Example
    -------
    >>> class MyView(TemplateMixin):
    ...     template = 'templates/home.html'

    """

    @property
    def _template(self):
        """ Returns the defined template which should be set using the
        ``template`` attribute on classes inheriting this view.

        Returns
        -------
        str
            Relative template path, e.g: ``templates/home.html``

        Raises
        ------
        NotImplementedError
            If ``self.template`` attribute is not defined

        """

        try:
            return self.template
        except AttributeError:
            raise NotImplementedError('template attribute is not defined')

    def render(self):
        """ Renders a template. This method will attempt to pass context
        to the template but if the ``context`` attribute does not exist then
        an empty dict will be passwed to the ``render_template`` method.

        Returns
        -------
        str
            Rendered template

        """

        return render_template(
            self._template,
            **getattr(self, 'context', {}))

    def get(self):
        """ Handle HTTP GET requets using Flask ``MethodView`` rendering a
        single html template.

        Returns
        -------
        str
            Rendered template

        """

        return self.render()