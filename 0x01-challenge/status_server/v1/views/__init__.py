#!/usr/bin/python3
""" Views module
"""
from api import v1
from v1 import views
from views import index
from index import *
from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
