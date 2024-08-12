
# Create your views here.
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_add(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    return render(request, 'todo_app/task_add.html', {'form': form})

def task_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'task_add.html')


def home(request):
    if request.method == 'POST':
        task_text = request.POST.get('task')
        if task_text:
            Task.objects.create(text=task_text)
        return redirect('home')

    tasks = Task.objects.all()
    return render(request, 'todo/home.html', {'tasks': tasks})

def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('home')
