from django.urls import path
from . import views

urlpatterns = [
    path('', views.worker, name="worker"),
    path('edit/<int:pk>', views.worker_edit, name="worker_edit"),
]