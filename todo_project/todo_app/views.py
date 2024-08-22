
# Create your views here.
from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


def homepage(request):
    if request.method == 'POST':
        new_task = request.POST.get('todo_item')
        if new_task:
            Task.objects.create(title=new_task)
        return redirect('homepage')
    tasks = Task.objects.all()
    return render(request, 'homepage.html', {'tasks': tasks})


def add_todo(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_todo.html')  # Redirect to the homepage after saving
    else:
        form = TaskForm()
    tasks = Task.objects.all()  # Fetch all tasks to display them
    return render(request, 'add_todo.html', {'form': form, 'tasks': tasks})


def task_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'task_add.html')
