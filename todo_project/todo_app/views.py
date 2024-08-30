
# Create your views here.
from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm


def index(request):
    signup_form = SignUpForm(request.POST)
    login_form = LoginForm(request.POST)

    if request.method == 'POST':
        if 'signup' in request.POST:
            signup_form = SignUpForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                username = signup_form.cleaned_data.get('username')
                password = signup_form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('homepage')
        elif 'login' in request.POST:
            login_form = LoginForm(request, data=request.POST)
            if login_form.is_valid():
                login(request, login_form.get_user())
                return redirect('homepage')
    else:
        signup_form = SignUpForm()
        login_form = LoginForm()

    return render(request, 'index.html', {
        'signup_form': signup_form,
        'login_form': login_form,
    })


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
