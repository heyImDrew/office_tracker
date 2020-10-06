from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('office', views.office, name='office'),
    path('office/edit/<int:pk>', views.office_edit, name='office_edit'),
    path('room', views.room, name='room'),
    path('book', views.book, name='book'),
]