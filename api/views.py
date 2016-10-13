from api.models import Location, Photo, Participant, FeedingRecord
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, serializers
from django.db.models import Q


def index(request):
    return render(request, 'api/index.html')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'latitude', 'longitude']

    def create(self, validated_data):
        location = Location(**validated_data)
        location.save()
        location.users.add(self.context['request'].user)
        return location


class LocationViewSet(viewsets.ModelViewSet):
    """
        Returns Locations owned by you.
    """
    serializer_class = LocationSerializer
    def get_queryset(self):
        return self.request.user.location_set.all()


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoViewSet(viewsets.ModelViewSet):
    """
        Returns Photos owned by you.
    """
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'


class ParticipantViewSet(viewsets.ModelViewSet):
    """
        Returns Participants owned by you.
    """
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()

class FeedingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedingRecord
        fields = '__all__'


class FeedingRecordViewSet(viewsets.ModelViewSet):
    """
        Returns FeedingRecords owned by you.
    """
    serializer_class = FeedingRecordSerializer
    queryset = FeedingRecord.objects.all()

    