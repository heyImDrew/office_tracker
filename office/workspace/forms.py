from django import forms
from .models import *

class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = ('number', 'street', 'house')

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('number', 'number_of_sits', 'office')

class BookForm(forms.ModelForm):
    class Meta:
        model = Booked
        fields = ('date', 'time_from', 'time_to', 'worker_at', 'room')