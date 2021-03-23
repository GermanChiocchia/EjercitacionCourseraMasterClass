from django.shortcuts import redirect, render
from .models import Task

# Create your views here.

def index(request):
    task_list = Task.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')

        task = Task(name=name, priority=priority)
        task.save()
        return redirect('/')

    return render(request, 'one_app/index.html', {'task_list': task_list})