from django.contrib import admin

# Register your models here.

from .models import Event
admin.site.register(Event) # Registering the Event model with the admin site
