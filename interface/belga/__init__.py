#!/usr/bin/env python
# -*- coding: utf-8 -*-

VERSION = (0, 1, 0)

__version__ = ".".join(map(str, VERSION))
__status__ = "Alpha"
__description__ = "Manager Antispam, Postfix, Dovecot"
__author__ = "Nillton OS <jniltinho@gmail.com>"
__email__ = "jniltinho@gmail.com"
__license__ = "MIT License"
__copyright__ = "Copyright 2013, BelgaProject"

import os
from werkzeug.utils import import_string
from flask import Flask

app = Flask(__name__)
app.config.from_object('belga.settings')

from belga.core.dashboard import mod as dashboard
app.register_blueprint(dashboard)



for mod_app in app.config['MOD_APPS']:
    #os.path.isfile(mod_dir + "/" + i + "/views.py")
    real_app = import_string('belga.modules.' + mod_app + '.' + mod_app)
    app.register_blueprint(real_app, url_prefix='/' + mod_app)

