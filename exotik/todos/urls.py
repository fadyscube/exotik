from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('old_todo/<str:date>/', views.old_todo, name='old_todo'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('remove_task/<int:id>/', views.remove_task, name='remove_task'),
    path('done_task/<int:id>/', views.done_task, name='done_task'),
    path('calendar/', views.calendar, name='calendar'),
    path('random_calendar/', views.random_calendar, name='random_calendar'),
]