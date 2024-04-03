from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'event_name', 'city_name', 'date', 'time', 'latitude', 'longitude')

