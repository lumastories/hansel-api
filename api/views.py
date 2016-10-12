from api.models import FeedingProgram, Profile
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, serializers
from django.db.models import Q


def index(request):
    return render(request, 'api/index.html')

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
        fields = ['name', 'country']

class FeedingProgramViewSet(UserCreateMixin, viewsets.ModelViewSet):
    """
        Returns FeedingPrograms owned by you or by someone in your team
    """
    serializer_class = FeedingProgramSerializer
    user_field = 'user'
    def get_queryset(self):
        team = self.request.user.profile.team
        return FeedingProgram.objects.filter(Q(user=self.request.user) | Q(user__profile__team=team))