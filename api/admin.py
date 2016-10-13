from django.contrib import admin
from api.models import *

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'age',)
    search_fields = ('name',)


admin.site.register(Profile)
admin.site.register(Location)
admin.site.register(Photo)
admin.site.register(FeedingRecord)
admin.site.register(Participant, ParticipantAdmin)
