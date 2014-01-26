# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
Create KEY

import hashlib
hashlib.md5("Flask_SMB4Manager").hexdigest()
068c2a771435c5c48fdf4a1cd9dfa465
"""

from datetime import timedelta
import os, sys

PROJECT_ROOT    = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT     = os.path.join(PROJECT_ROOT, 'static')
MAP_STATIC_ROOT = ('/robots.txt', '/favicon.ico')
NOME            = "Belga Manager Antispam"
DEBUG           = True
TESTING         = False
SECRET_KEY      = '068c2b781435c5c48fdf4a1cd9dfa465'
CSRF_ENABLED    = True
PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)

CORE_APPS = ['belga.core.dashboard']

mod_dir  = os.path.join(PROJECT_ROOT, 'modules')
MOD_APPS = [ name for name in os.listdir(mod_dir) if os.path.isdir(os.path.join(mod_dir, name)) and os.path.isfile(os.path.join(mod_dir, name + "/views.py")) ]


LOGGER_ENABLED = False
LOGGER_LEVEL = 'DEBUG'
LOGGER_FORMAT = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
LOGGER_DATE_FORMAT = '%d.%m %H:%M:%S'
