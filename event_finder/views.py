import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view
from data_creation.models import Event
from data_creation.serializers import EventSerializer
import datetime


@api_view(['GET'])
def find_events(request):
    # Retrieve user's location and search date from request data
    user_latitude = request.data.get('latitude')
    user_longitude = request.data.get('longitude')
    search_date = request.data.get('date')

    print('user_latitude:', user_latitude, 'user_longitude:', user_longitude, 'search_date:', search_date)

    # Retrieve events occurring within the next 14 days from the specified date
    search_date = datetime.datetime.strptime(search_date, '%Y-%m-%d').date()
    end_date = search_date + datetime.timedelta(days=14)

    print('search_date:', search_date, 'end_date:', end_date)

    events = Event.objects.filter(date__range=[search_date, end_date])

    # Sort events by the earliest event after the specified date
    events = events.order_by('date')

    total_events = events.count()  # Count total events
    total_pages = (total_events + 9) // 10  # Calculate total pages

    result = {}

    for page in range(total_pages):

        event_data = [] * 10  # Create a list to store event data for the current page

        # Calculate start and end index for events based on page number
        start_index = page * 10
        end_index = start_index + 10

        # Retrieve events for the current page
        current_events = events[start_index:end_index]

        for event in current_events:
            # Retrieve weather conditions for the event
            weather = get_weather(event.city_name, event.date)

            # Calculate distance between user's location and event location
            distance_km = calculate_distance(user_latitude, user_longitude, event.latitude, event.longitude)

            # Serialize event data
            event_serializer = EventSerializer(event)

            # Create event data with weather and distance
            event_data.append(
                {'event_name': event_serializer.data['event_name'],
                 'city_name': event_serializer.data['city_name'],
                 'date': event_serializer.data['date'],
                 'weather': weather,
                 'distance_km': distance_km}
            )
        # Add event data to result
        result["Page" + str(page + 1)] = {  # for 1st line we included the page number
            'events': event_data,  # events are key for all events stored in event_data list
            'page': page + 1,
            'pageSize': 10,
            'totalEvents': total_events,
            'totalPages': total_pages
        }

    # Return paginated response
    return JsonResponse(result)


def get_weather(city_name, date):
    # Make request to Weather API
    response = requests.get(
        'https://gg-backend-assignment.azurewebsites.net/api/Weather',
        params={
            'code': "KfQnTWHJbg1giyB_Q9Ih3Xu3L9QOBDTuU5zwqVikZepCAzFut3rqsg==",
            'city': city_name,
            'date': date.strftime('%Y-%m-%d')
        }
    )
    # print(response.text) was used to check the response
    data = response.json()
    # Return weather data if available
    return data['weather'] if response.status_code == 200 else 'Weather unavailable'


def calculate_distance(latitude1, longitude1, latitude2, longitude2):
    # Make request to Distance Calculation API
    response = requests.get(
        'https://gg-backend-assignment.azurewebsites.net/api/Distance',
        params={
            'code': 'IAKvV2EvJa6Z6dEIUqqd7yGAu7IZ8gaH-a0QO6btjRc1AzFu8Y3IcQ==',
            'latitude1': latitude1,
            'longitude1': longitude1,
            'latitude2': latitude2,
            'longitude2': longitude2
        }
    )
    # print(response.text) was used to check the response
    data = response.json()
    # Return distance if available
    return data['distance'] if response.status_code == 200 else None
