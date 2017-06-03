from django.contrib import admin

# Register your models here.

from .models import Route, Stop, Prediction

admin.site.register(Route)
admin.site.register(Stop)
admin.site.register(Prediction)
