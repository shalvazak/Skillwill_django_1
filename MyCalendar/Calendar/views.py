from django.http import JsonResponse
from django.shortcuts import render

from Calendar.models import CalendarEvent


# Create your views here.
def get_calendar_event(request):
    event = CalendarEvent.objects.first()
    if event:
        return JsonResponse({"year": event.date.year, "month": event.date.month, "day": event.date.day})
    return JsonResponse({"error": "No event found"})