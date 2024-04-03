from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.event_list, name='event_list'),
    path('list/', views.event_list, name='event_list'),
    path('list/<int:id>/', views.event_list, name='event_details'),  # Endpoint to list event details by ID
]
