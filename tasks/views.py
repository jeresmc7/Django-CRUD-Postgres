from pydoc import describe
from turtle import title
from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

def list_tasks(request):
    tasks = Task.objects.all() # Esto retorna una lista de objetos
    return render(request, 'list_tasks.html', {'tasks': tasks})

def create_task(request):
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save()
    # print(request.POST)
    return redirect('/tasks/')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')