from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    taskInOrder = Task.objects.order_by("priority", "dueDate")
    return render(request, "index.html", {"taskInOrder": taskInOrder})

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
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