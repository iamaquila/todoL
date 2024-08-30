from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
