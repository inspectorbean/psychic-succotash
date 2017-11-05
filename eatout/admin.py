from django.contrib import admin

# Register your models here.

from .models import Dinner, Restaurant, Mood

admin.site.register(Dinner)
admin.site.register(Restaurant)
admin.site.register(Mood)
