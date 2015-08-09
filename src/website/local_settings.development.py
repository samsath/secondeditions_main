# -*- coding: utf-8 -*-
from default_settings import *

import os
path = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = ('127.0.0.1',)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'secondeditions',
        'USER': 'secondeditionsdb',
        'PASSWORD': 'Tiesenlap13',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'info@secondeditions.net'

# Make this unique, and don't share it with anybody.
SECRET_KEY = u'93g)$@ia@r6t27yw70-^*-42jih=u#1r1ox72^#d5)st=b)m!t'


#INSTALLED_APPS = INSTALLED_APPS + (
#    'debug_toolbar',
#)
