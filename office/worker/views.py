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
            else: return render(request, 'worker.html', {
                'form':WorkerForm(),
                'workers':Worker.objects.all(),
                'msg':True,
                })
    return render(request, 'worker.html', {
        'form':WorkerForm(),
        'workers':Worker.objects.all().order_by('id'),
        'msg':False,
        })

def valid_name(name):
    if name.isalpha():
        return True
    else:
        return False

def worker_edit(request, pk):
    if request.method == "POST":
        form = WorkerForm(request.POST)
        if form.is_valid():
            if valid_name(request.POST['name']) and valid_name(request.POST['last_name']):
                worker = Worker.objects.get(id = pk)
                worker.name = request.POST['name']
                worker.last_name = request.POST['last_name']
                worker.save()
                workers = Worker.objects.all()
                return redirect('worker')
            else: return render(request, 'worker_edit.html', {
                'form':WorkerForm(),
                'worker':Worker.objects.get(id = pk),
                'msg':True,
                })
    return render(request, 'worker_edit.html', {
        'form':WorkerForm(),
        'worker':Worker.objects.get(id = pk),
        'msg':False,
        })

def worker_delete(request, pk):
    worker = Worker.objects.get(id = pk)
    worker.delete()
    return redirect('worker')