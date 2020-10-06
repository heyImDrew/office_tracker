from django.shortcuts import render, redirect
from .forms import OfficeForm, RoomForm, BookForm
from .models import *
from worker.models import Worker
import datetime

def default(request):
    return render(request, 'default.html', {})

def office(request):
    if request.method == "POST":
        form = OfficeForm(request.POST)
        if form.is_valid():
            if int(request.POST['number']) not in [office.number for office in Office.objects.all()]:
                office = form.save()
                office.save()
    form = OfficeForm()
    offices = Office.objects.all()
    return render(request, 'office.html', {'form':form,'offices':offices,})

def office_edit(request, pk):
    if request.method == "POST":
        form = OfficeForm(request.POST)
        if form.is_valid():
            office = Office.objects.get(id = pk)
            office.number = request.POST['number']
            office.address = request.POST['address']
            office.save()
            office = Office.objects.all()
            return redirect('office')
    return render(request, 'office_edit.html', {'form':OfficeForm(),'office':Office.objects.get(id = pk),})

# def worker_delete(request, pk):
#     worker = Worker.objects.get(id = pk)
#     worker.delete()
#     return redirect('worker')

def room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            room.save()
    form = RoomForm()
    rooms = Room.objects.all()
    return render(request, 'room.html', {'form':form, 'rooms':rooms})

def book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            f_room = request.POST['room']
            f_date = request.POST['date']
            f_time_from = request.POST['time_from']
            f_time_to = request.POST['time_to']
            f_worker = request.POST['worker_at']
            if (book_available_check(int(f_room), f_date, int(f_time_from), int(f_time_to)) == True):
                book = form.save()
                book.save()
                worker = Worker.objects.get(id = int(f_worker))
                worker.booked_history.add(book)
            else:
                books = Booked.objects.all()
                return render(request, 'book.html', {'form':form, 'books':books, 'msg':'No free spots at this time!'})
    form = BookForm()
    books = Booked.objects.all()
    return render(request, 'book.html', {'form':form, 'books':books,})

def book_available_check(room_id, f_date, time_from, time_to):
    room_now = Room.objects.get(id = room_id)
    max_sits = room_now.number_of_sits
    other_books = list(Booked.objects.filter(room = room_now, date = datetime.datetime.strptime(f_date, "%Y-%m-%d").date()))
    hours = [h for h in range(time_from, time_to)]
    booked_hours = []
    for book in other_books:
        booked_hours.append([h for h in range(book.time_from, book.time_to)])
    for x in hours:
        count = 0
        for l in booked_hours:
            if x in l:
                count += 1
        if count < 3:
            pass
        else:
            return False
    return True