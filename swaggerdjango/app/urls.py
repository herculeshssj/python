# app - urls.py file

from django.urls import path
from app.views import *

urlpatterns = [
    path('demo/',first_view, name='demo'),
    path('second/', Second.as_view(), name='first_view'),
]