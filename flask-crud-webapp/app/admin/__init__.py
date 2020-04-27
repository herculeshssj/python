# app/admin/__init__.py

from . import views
from flask import Blueprint

admin = Blueprint('admin', __name__)
