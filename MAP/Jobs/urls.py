from django.urls import path
from .views import indexPageView, joblistingPageView, joblistingdetailsPageView

urlpatterns = [
    path("", indexPageView, name="landing"),
    path("joblisting/", joblistingPageView, name="job_listing"),
    path("joblistingdetails/<int:joblistingID>/", joblistingdetailsPageView, name="job_listing_details")    
]   