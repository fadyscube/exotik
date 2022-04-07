from unicodedata import name
from django.urls import path

from . import views

app_name = 'activities'

urlpatterns = [
    path('random/', views.random, name='random'),
]