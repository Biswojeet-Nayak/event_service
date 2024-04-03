# event_finder/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('find/', views.find_events, name='find-events'),
]
