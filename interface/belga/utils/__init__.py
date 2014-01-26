# -*- coding: utf-8 -*-
from functools import wraps
from flask import flash, request, render_template, url_for



def render(template_name, **kwargs):
      print __package__.split('.')[-1::]
      return render_template(template_name, **kwargs)

