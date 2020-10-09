from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('office', views.office, name='office'),
    path('office/edit/<int:pk>', views.office_edit, name='office_edit'),
    path('office/delete/<int:pk>', views.office_delete, name='office_delete'),
    path('room', views.room, name='room'),
    path('room/edit/<int:pk>', views.room_edit, name='room_edit'),
    path('room/delete/<int:pk>', views.room_delete, name='room_delete'),
    path('book', views.book, name='book'),
]