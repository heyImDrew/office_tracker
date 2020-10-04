from rest_framework import serializers
from worker.models import Worker
from workspace.models import Office, Room, Booked

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class BookedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booked
        fields = "__all__"