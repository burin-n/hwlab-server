from django.contrib import admin

# Register your models here.

from .models import State,Setting

admin.site.register(State)
admin.site.register(Setting)