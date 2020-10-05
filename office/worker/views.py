from django.shortcuts import render, redirect
from .forms import WorkerForm
from .models import Worker

def worker(request):
    if request.method == "POST":
        form = WorkerForm(request.POST)
        if form.is_valid():
            if valid_name(request.POST['name']) and valid_name(request.POST['last_name']):
                worker = form.save()
                worker.name = request.POST['name'].lower().capitalize()
                worker.last_name = request.POST['last_name'].lower().capitalize()
                worker.save()
    form = WorkerForm()
    workers = Worker.objects.all()
    return render(request, 'worker.html', {'form':form,'workers':workers,})

def valid_name(name):
    if name.isalpha():
        return True
    else:
        return False

def worker_edit(request, pk):
    if request.method == "POST":
        form = WorkerForm(request.POST)
        if form.is_valid():
            worker = Worker.objects.get(id = pk)
            worker.name = request.POST['name']
            worker.last_name = request.POST['last_name']
            worker.save()
            workers = Worker.objects.all()
            return redirect('worker')
    return render(request, 'worker_edit.html', {'form':WorkerForm(),'worker':Worker.objects.get(id = pk),})

def worker_delete(request, pk):
    worker = Worker.objects.get(id = pk)
    worker.delete()
    return redirect('worker')