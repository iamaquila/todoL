from django.urls import path
from todo_app import views
from .views import task_list, task_add


urlpatterns = [
    path('task_list/', task_list, name='task_list'),
    path('add/', task_add, name='task_add'),
    path('', views.homepage, name='homepage'),
    path('add_todo/', views.add_todo, name='add_todo'),
]
