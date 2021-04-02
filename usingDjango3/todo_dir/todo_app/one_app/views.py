from django.shortcuts import redirect, render
from .models import Task

# Create your views here.

def index(request):
    task_list = Task.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
        return redirect('/')

    return render(request, 'one_app/index.html', {'task_list': task_list})


def delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'one_app/delete.html',{'task': task})
