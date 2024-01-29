from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Task

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')
