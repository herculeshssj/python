from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/sobre/', views.sobre, name='sobre')
]
