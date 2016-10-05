from api.models import FeedingProgram, Profile
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, serializers


class UserCreateMixin(object):
    """
    By default the user field is "user" you can change it
    to your model "user" field.

    Usage:
    class PostViewSet(UserCreateMixin, viewsets.ModelViewSet):
    # ViewsSet required info...
    user_field = 'creator'
    """
    user_field = 'user'

    def get_user_field(self):
        """
        You can dynamically change the user field
        """
        return self.user_field

    def perform_create(self, serializer):
        kwargs = {
            self.get_user_field(): self.request.user
        }
        serializer.save(**kwargs)


class FeedingProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedingProgram
        fields = '__all__' #['name', 'country']

class FeedingProgramViewSet(UserCreateMixin, viewsets.ModelViewSet):
    serializer_class = FeedingProgramSerializer
    user_field = 'user'
    def get_queryset(self):
        return FeedingProgram.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        kwargs = {
          'user': self.request.user # Change 'user' to you model user field.
        }
        serializer.save(**kwargs)