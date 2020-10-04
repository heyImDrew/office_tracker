from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.mixins import *

from worker.models import Worker
from workspace.models import Office, Room, Booked
from .serializers import WorkerSerializer, OfficeSerializer, RoomSerializer, BookedSerializer

class WorkerView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class WorkerUpdate(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

class OfficeView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OfficeUpdate(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

class RoomView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RoomUpdate(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

class BookedView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Booked.objects.all()
    serializer_class = BookedSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookedUpdate(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Booked.objects.all()
    serializer_class = BookedSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)