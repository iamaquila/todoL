# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Task
from .forms import TaskForm
from .models import TodoItem


def homepage(request, todolist=None):
    todo_items = TodoItem.objects.all()
    if request.method == 'POST':
        new_task = request.POST.get('task')
        if new_task:
            Task.objects.create(title=new_task)
        return redirect('homepage')
    tasks = Task.objects.all()
    return render(request, 'homepage.html', {'todolist': todolist})


def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_lists')  # Redirects to the view named 'task_list'
    else:
        form = TaskForm()
    return render(request, 'task_add', {'form': form})


def add_todo(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new task to the database
            return redirect(reverse('homepage'))  # Redirect to the task list page
    else:
        form = TaskForm()

    return render(request, 'todo_app/add_todo.html', {'form': form})

def homepage(request):
    return render(request, 'homepage.html')