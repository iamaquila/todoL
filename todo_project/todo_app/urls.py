from django.contrib.auth import views
from django.urls import path
from .views import task_add



urlpatterns = [
    path('add/', task_add, name='task_add'),
    path('', views.homepage, name='homepage'),
    path('add_todo/', views.add_todo, name='add_todo'),
]
