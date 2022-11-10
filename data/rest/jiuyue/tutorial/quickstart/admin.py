from django.contrib import admin
from quickstart.models import *
# Register your models here.

class Type1Admin(admin.ModelAdmin):
  list_display = ('name', 'logo', 'index')
  
class DetailAdmin(admin.ModelAdmin):
  list_display = (
    'name',
    'logo',
    'desc',
    'index',
    'type'
    )
admin.site.register(Type1, Type1Admin)
admin.site.register(Detail, DetailAdmin)