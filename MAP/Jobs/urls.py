from django.urls import path
from .views import indexPageView, joblistingPageView

urlpatterns = [
    path("", indexPageView, name="landing"),
    path("joblisting/", joblistingPageView, name="job_listing")   
    #edit
    # add
    #  
]   