from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indexPageView(request) :
    return HttpResponse("Hello")

def joblistingPageView(request) :
    return render(request, "Jobs/job_listing.html")