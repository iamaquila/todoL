from django.urls import path
from .views import task_list, task_add

urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', task_add, name='task_add'),
]
