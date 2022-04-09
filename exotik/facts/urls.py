from django.urls import path

from . import views

app_name = 'facts'

urlpatterns = [
    path('', views.index, name='index')
]