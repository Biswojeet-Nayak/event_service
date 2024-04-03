from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer


# view file that handles both GET and POST requests for events
@api_view(['GET', 'POST'])
def event_list(request, id=None):
    """
    List all events or create a new event.
    """
    if request.method == 'GET':
        # If an ID is provided, retrieve the specific event
        if id:
            try:
                event = Event.objects.get(id=id)
                serializer = EventSerializer(event)
                return Response(serializer.data)
            # If event doesn't exist, return a 404 response
            except Event.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        # If no ID provided, retrieve all events
        else:
            events = Event.objects.all()
            serializer = EventSerializer(events, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        # Create a new event
        serializer = EventSerializer(data=request.data)
        # If the data is valid, save the event and return a 201 response
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If data is not valid, return a 400 response with errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
