from django.shortcuts import render, redirect
from .forms import WorkerForm
from .models import Worker

def worker(request):
    if request.method == "POST":
        form = WorkerForm(request.POST)
        if form.is_valid():
            worker = form.save()
            worker.save()
    form = WorkerForm()
    workers = Worker.objects.all()
    return render(request, 'worker.html', {'form':form,'workers':workers,})

def worker_edit(request, pk):
    if request.method == "POST":
        form = WorkerForm(request.POST)
        if form.is_valid():
            worker = Worker.objects.get(id = pk)
            worker.name = request.POST['name']
            worker.last_name = request.POST['last_name']
            worker.save()
            workers = Worker.objects.all()
            return render(request, 'default.html')  
    form = WorkerForm()
    worker = Worker.objects.get(id = pk)
    return render(request, 'worker_edit.html', {'form':form,'worker':worker,})   