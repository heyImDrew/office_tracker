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