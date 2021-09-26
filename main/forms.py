from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        
        for value in ('first_name', 'last_name', 'email'):
            model._meta.get_field(value).blank = False
            model._meta.get_field(value).null = False
        model._meta.get_field('email')._unique = True

        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline']
