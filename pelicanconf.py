#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Olivier Larchev\xeaque'
SITENAME = u'Olivier Larchev\xeaque'

I18N_SUBSITES = {
    'fr': {
        'SITENAME': SITENAME,
        },
    'en': {
        'SITENAME': SITENAME,
        },
}

languages_lookup = {
    'en': 'English',
    'fr': 'Français',
}


def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]


def my_ordered_items(dict):
    items = list(dict.items())
    # swap first and last using tuple unpacking
    items[0], items[-1] = items[-1], items[0]
    return items

JINJA_FILTERS = {
    'lookup_lang_name': lookup_lang_name,
    'my_ordered_items': my_ordered_items,
}

SITEURL = 'http://olarcheveque.github.io'


PATH = 'content'

TIMEZONE = 'America/Montreal'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGIN_PATHS = ["../pelican-plugins", ]
PLUGINS = ['i18n_subsites', ]

THEME = '../pelican-svbtle/'

AUTHOR_BIO = 'Développeur Web Python'

GOOGLE_ANALYTICS = 'UA-53293823-1'
