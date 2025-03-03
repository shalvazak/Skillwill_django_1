from django.urls import path
from .views import get_calendar_event

urlpatterns = [
    path('', get_calendar_event, name='calendar_event'),
]
