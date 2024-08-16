from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def homepage(request):
    if request.method == 'POST':
        new_task = request.POST.get('task')
        if new_task:
            Task.objects.create(title=new_task)
        return redirect('homepage')
    tasks = Task.objects.all()
    return render(request, 'homepage.html', {'tasks': tasks})


def task_list(request):
    tasks = Task.objects.all()
    return render(request,'todo_app/task_list.html', {'tasks': tasks})

from django.shortcuts import redirect

def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirects to the view named 'task_list'
    else:
        form = TaskForm()
    return render(request, 'todo_project/todo_app/templates/todo_app/task_add.html', {'form': form})

def homepage(request):
    return render(request, 'homepage.html')

def add_todo(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new task to the database
            return redirect('task_list')  # Redirect to the task list page
    else:
        form = TaskForm()

    return render(request, 'todo_app/add_todo.html', {'form': form})