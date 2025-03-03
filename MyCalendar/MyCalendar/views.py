from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to MyCalendar</h1><p>Use /calendar/ to see the date and /user/ to see user info.</p>")
