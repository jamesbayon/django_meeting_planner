from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from meetings.models import Meeting


# Create your views here.

def welcome(request):
    meetings = Meeting.objects.all()

    return render(request, "website/welcome.html",
                  {"meetings": meetings})

def date(request):
    return HttpResponse("This page was served at: " + str(datetime.now()))

def about(request):
    return HttpResponse("Hi! I am James")