from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('old_todo/<str:date>/', views.old_todo, name='old_todo'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('remove_task/<int:id>/', views.remove_task, name='remove_task'),
    path('tasks_list/', views.tasks_list, name='tasks_list'),
    path('calendar/', views.calendar, name='calendar'),
]