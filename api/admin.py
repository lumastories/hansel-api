from django.contrib import admin
from api.models import *

class KidAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'weight', 'age',)
    search_fields = ('first_name', 'last_name',)

admin.site.register(Kid, KidAdmin)
