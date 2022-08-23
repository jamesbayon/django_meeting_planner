from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from meetings.models import Meeting


# Create your views here.

def welcome(request):
    num_meetings = Meeting.objects.count()

    return render(request, "website/welcome.html",
                  {"num_meetings": num_meetings})

def date(request):
    return HttpResponse("This page was served at: " + str(datetime.now()))

def about(request):
    return HttpResponse("Hi! I am James")