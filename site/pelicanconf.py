#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Diogo Munaro Vieira'
SITENAME = u'Diogo Munaro Vieira'
SITEURL = 'http://diogomunaro.com'

PATH = 'content'
OUTPUT_PATH = '../'
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

THEME = 'crowsfoot'

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
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# Following items are often useful when publishing

GITHUB_ADDRESS = 'http://github.com/dmvieira/'
EMAIL_ADDRESS = 'diogo.mvieira@gmail.com'
TWITTER_ADDRESS = 'https://twitter.com/diogomvieira'
FB_ADDRESS = 'https://pt-br.facebook.com/munarovieira'
LINKEDIN_ADDRESS = 'https://br.linkedin.com/in/dmvieira'
PROFILE_IMAGE_URL = 'https://pt.gravatar.com/userimage/34518379/821607f3755e2bf394491f052ed24d2e.jpg?size=400'

DISQUS_SITENAME = "diogomunaro"
GOOGLE_ANALYTICS = "UA-58403599-1"
