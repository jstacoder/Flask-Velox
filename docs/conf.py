# -*- coding: utf-8 -*-

"""
.. module:: docs
   :synopsis: Sphinx documentation configuration
"""

import sys
import os

# Add flask_velox to the Path
root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
    )
)

sys.path.append(os.path.join(root, 'flask_velox'))

import flask_velox  # noqa


# Project details
project = u'Flask-Velox'
copyright = u'2014, SOON_'
version = '0.0.1'
release = '0.0.1'

# Sphinx Config
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

extensions = [
    'sphinxjp.themes.basicstrap',
    'sphinx.ext.autodoc',
    'sphinxcontrib.napoleon',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig']

exclude_patterns = []

# Theme
html_theme = 'basicstrap'
html_theme_options = {
    'inner_theme': True,
    'inner_theme_name': 'bootswatch-cerulean'
}
#html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
#html_static_path = ['_static']
#html_theme_options = {
#    'bootswatch_theme': 'Lumen',
#    'bootstrap_version': '3',
#}
#pygments_style = 'sphinx'
#htmlhelp_basename = 'Flask-Velox'
