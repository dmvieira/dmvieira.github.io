#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Diogo Munaro Vieira'
SITENAME = u'Diogo Munaro Vieira'
SITESUBTITLE = u'Because Programming is Cool and IT needs simplicity'
SITEURL = 'http://diogomunaro.com'
RELATIVE_URLS = True
MENUITEMS = [('Home', '/')]

PATH = 'content'
STATIC_PATHS = ['images']
OUTPUT_PATH = '../'
ARTICLE_PATHS = ['blog']
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

THEME = 'crowsfoot'

TIMEZONE = 'America/Sao_Paulo'
LOCALE = ['en_US.utf8']
DEFAULT_LANG = u'en'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# Following items are often useful when publishing

GITHUB_ADDRESS = 'http://github.com/dmvieira/'
EMAIL_ADDRESS = 'diogo.mvieira@gmail.com'
TWITTER_ADDRESS = 'https://twitter.com/diogomvieira'
#FB_ADDRESS = 'https://pt-br.facebook.com/munarovieira'
LINKEDIN_ADDRESS = 'https://br.linkedin.com/in/dmvieira'
PROFILE_IMAGE_URL = 'https://pt.gravatar.com/userimage/34518379/821607f3755e2bf394491f052ed24d2e.jpg?size=400'

DISQUS_SITENAME = "diogomunaro"
GOOGLE_ANALYTICS = "UA-58403599-1"

PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}