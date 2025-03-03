from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import UserProfile

def get_user_info(request):
    user = UserProfile.objects.first()
    if user:
        return JsonResponse({
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": user.age()
        })
    return JsonResponse({"error": "User not found"})
