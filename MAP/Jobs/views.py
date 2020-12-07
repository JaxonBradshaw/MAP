from django.shortcuts import render
from django.http import HttpResponse
from .models import Job_Listing, Job_Offer, Job_Application

# Create your views here.

def indexPageView(request) :
    return HttpResponse("Hello")

def joblistingPageView(request) :
    data = Job_Listing.objects.all()

    context = {
        "joblisting" : data
    }
    return render(request, "Jobs/job_listing.html", context)

def joblistingdetailsPageView(request, joblistingID) :
    data = Job_Listing.objects.get(id=joblistingID)

    context = {
        "joblisting" : data
    }

    return render(request, 'Jobs/job_listing_details.html', context)

def editjoblistingPageView(request, joblistingID) :
    data = Job_Listing.objects.get(id=joblistingID)

    context = {
        "joblisting" : data
    }

    return render(request, 'Jobs/edit_job_listing.html', context)
