from django.contrib import admin
from .models import *

# Register your models here.
class QueryAdmin(admin.ModelAdmin):
    list_display = ['statement', 'is_harrassing']
    list_filter = ['is_harrassing']
    list_editable = ['is_harrassing']

admin.site.register(query, QueryAdmin)
