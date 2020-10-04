from django.urls import path
from .views import *

urlpatterns = [
    path('workers/', WorkerView.as_view(), name="api_workers"),
    path('workers/<int:pk>', WorkerUpdate.as_view()),
    path('offices/', OfficeView.as_view(), name="api_offices"),
    path('offices/<int:pk>', OfficeUpdate.as_view()),
    path('rooms/', RoomView.as_view(), name="api_rooms"),
    path('rooms/<int:pk>', RoomUpdate.as_view()),
    path('booked/', BookedView.as_view(), name="api_booked"),
    path('booked/<int:pk>', BookedUpdate.as_view()),
]