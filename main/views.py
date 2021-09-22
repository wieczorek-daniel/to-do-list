from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import CreateUserForm


def index(request):
    return render(request, "main/index.html")

def login(request):
    return render(request, "main/login.html")

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
         form = CreateUserForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             messages.success(request, f'An account has been created for user {username}.')
             return redirect('login')

    context = {'form': form}
    return render(request, "main/register.html", context)
