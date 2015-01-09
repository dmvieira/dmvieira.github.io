#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Diogo Munaro Vieira'
SITENAME = u'Diogo Munaro Vieira'
SITEURL = 'http://diogomunaro.com'

PATH = 'content'
OUTPUT_PATH = '../'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5


SITEURL = 'http://diogomunaro.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# Following items are often useful when publishing

PDF_GENERATOR = True
GITHUB_URL = 'http://github.com/dmvieira/'
DISQUS_SITENAME = "diogomunaro.disqus.com"
GOOGLE_ANALYTICS = "UA-58403599-1"
