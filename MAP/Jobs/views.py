from django.shortcuts import render
from django.http import HttpResponse
from .models import Job_Listing

# Create your views here.

def indexPageView(request) :
    return HttpResponse("Hello")

def testView(request) :
    data = Job_Listing.objects.all()
    return render()