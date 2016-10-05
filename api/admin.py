from django.contrib import admin
from api.models import *

class KidAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'weight', 'age',)
    search_fields = ('first_name', 'last_name',)


admin.site.register(Profile)
admin.site.register(FeedingProgram)
admin.site.register(Location)
admin.site.register(Photo)
admin.site.register(Day)
admin.site.register(FeedingRecord)
admin.site.register(Kid, KidAdmin)
