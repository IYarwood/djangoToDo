from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.template import loader
from .models import Task
from .forms import TaskForm, newUserForm
from django.contrib import messages


# Create your views here.
def newUser(request, *args, **kwargs):
    if request.method == 'POST':
        form = newUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logIn')
    else:
        form = newUserForm()
    return render(request, "newUser.html", {"form": form})

def logIn(request, *args, **kwargs):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        #If authenticated, login (Django function) and redirect to hub
        #If not give error 
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "logIn.html")

def index(request):
    user = request.user
    userID = user.id
    taskInOrder = Task.objects.filter(userID=userID).order_by("priority", "dueDate")
    return render(request, "index.html", {"taskInOrder": taskInOrder})

def newTask(request):
    if request.method == 'POST':
        user =request.user
        print(user)
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.userID = user.id
            task.save()
        return redirect('index')
    else:
        form = TaskForm()
    
    return render(request, "newTask.html", {'form': form})
 
def update(request, *args, **kwargs):
    id = kwargs['id']
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)

    return render(request, 'update.html', {'form': form})

def delete(request, *args, **kwargs):
    id = kwargs['id']
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('index')