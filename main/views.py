from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, UpdateUserForm, CreateTaskForm
from .models import Task


def index(request):
    return render(request, "main/index.html")


def loginUser(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('dashboard')
			else:
				messages.error(request, 'The username or password is incorrect.')

		context = {}
		return render(request, 'main/login.html', context)


def registerUser(request):
    if request.user.is_authenticated:
	    return redirect('dashboard')
    else:
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


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    tasks = Task.objects.filter(owner=request.user).all()
    context = {'tasks': tasks}
    return render(request, "main/dashboard.html", context)


@login_required(login_url='login')
def settings(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)

        if form.is_valid():
            messages.success(request, 'User data has been updated.')
            form.save()
            return redirect('settings')
        else:
            messages.error(request, 'An error occurred while updating an user.')
            return redirect('settings')
    else:
        form = UpdateUserForm(instance=request.user)
        context = {'form': form}
        return render(request, 'main/settings.html', context)


@login_required(login_url='login')
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            messages.success(request, 'A password has been updated.')
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('settings')
        else:
            messages.error(request, 'An error occurred while updating a password.')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)

        context = {'form': form}
        return render(request, 'main/change_password.html', context)


@login_required(login_url='login')
def createTask(request):
    form = CreateTaskForm()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            messages.success(request, 'A task has been created.')
            return redirect('dashboard')

    context = {'form': form}
    return render(request, "main/create_task.html", context)


@login_required(login_url='login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    
    if request.method == "POST":
        form = CreateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'A task has been updated.')
            return redirect('dashboard')

    messages.error(request, 'An error occurred while updating a task.')
    return redirect('dashboard')


@login_required(login_url='login')
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    
    if request.method == "POST":
        task.delete()
        messages.success(request, 'A task has been deleted.')
        return redirect('dashboard')

    messages.error(request, 'An error occurred while deleting a task.')
    return redirect('dashboard')
