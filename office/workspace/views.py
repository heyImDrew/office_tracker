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
            if (int(request.POST['number']) not in [office.number for office in Office.objects.all()]) and (request.POST['street'].isalpha()):
                office = form.save()
                office.street = request.POST['street'].lower().capitalize()
                office.save()
            else: return render(request, 'office.html', {'form':OfficeForm(),'offices':Office.objects.all().order_by('number'),'msg':True,})
    form = OfficeForm()
    offices = Office.objects.all().order_by('number')
    return render(request, 'office.html', {'form':form,'offices':offices,'msg':False})

def office_edit(request, pk):
    if request.method == "POST":
        form = OfficeForm(request.POST)
        if form.is_valid():
            if (int(request.POST['number']) not in [office.number for office in Office.objects.all() if office.number!=Office.objects.get(id=pk).number]) and (request.POST['street'].isalpha()):
                office = Office.objects.get(id = pk)
                office.number = request.POST['number']
                office.street = request.POST['street'].lower().capitalize()
                office.house = request.POST['house']
                office.save()
                return redirect('office')
            else: 
                return render(request, 'office_edit.html', {'form':OfficeForm(),'office':Office.objects.get(id = pk),'msg':True,})
    return render(request, 'office_edit.html', {'form':OfficeForm(),'office':Office.objects.get(id = pk),'msg':False})

def office_delete(request, pk):
    office = Office.objects.get(id = pk)
    office.delete()
    return redirect('office')

def room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            if (int(request.POST['number']) not in [room.number for room in Room.objects.filter(office = Office.objects.get(id = int(request.POST['office'])))]):
                room = form.save()
                room.save()
            else:
                return render(request, 'room.html', {'form':RoomForm(), 'rooms':Room.objects.all(), 'msg':True})
    form = RoomForm()
    rooms = Room.objects.all()
    return render(request, 'room.html', {'form':form, 'rooms':rooms, 'msg':False})

def room_edit(request, pk):
    if request.method == "POST":
        import pdb; pdb.set_trace();
        form = RoomForm(request.POST)
        if form.is_valid():
            if int(request.POST['number']) not in [x.number for x in Room.objects.filter(office = Office.objects.get(id = int(request.POST['office'])))]:
                room = Room.objects.get(id = pk)
                room.number = request.POST['number']
                room.office = Office.objects.get(id = int(request.POST['office']))
                room.number_of_sits = request.POST['number_of_sits']
                room.save()
            else: 
                return render(request, 'room_edit.html', {'form':RoomForm(),'room':Room.objects.get(id = pk),'msg':True})
    return render(request, 'room_edit.html', {'form':RoomForm(),'room':Room.objects.get(id = pk),'msg':False})

def room_delete(request, pk):
    room = Room.objects.get(id = pk)
    room.delete()
    return redirect('room')

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