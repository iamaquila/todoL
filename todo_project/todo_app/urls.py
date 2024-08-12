from django.urls import path,  include
from .views import task_list, task_add
from . import views

urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', task_add, name='task_add'),
    # path('', include('todo.urls')),
]
    

