#!/usr/bin/env python
# -*- coding: utf-8 -*

from belga.core.app import BelgaModule
from flask import render_template, request, redirect, url_for, abort, session, jsonify

mod = BelgaModule("dashboard", __name__)

from .views import *
