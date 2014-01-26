

from belga.core.app import BelgaModule
from flask import render_template, request, redirect, url_for, abort, session, jsonify

from belga.utils import *

antispam = BelgaModule("antispam", __name__)


from .views import *
