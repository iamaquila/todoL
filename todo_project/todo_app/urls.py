from django.urls import path
from . import views
from .views import task_add


urlpatterns = [
    path('', views.index, name='index'),
    path('/homepage', views.homepage, name='homepage'),
    path('add/', task_add, name='task_add.html'),
    path('add_todo/', views.add_todo, name='add_todo'),
]
