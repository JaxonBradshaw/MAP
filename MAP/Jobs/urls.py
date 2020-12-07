from django.urls import path
from .views import indexPageView, joblistingPageView

urlpatterns = [
    path("", indexPageView, name="landing"),
    path("", joblistingPageView, name="job_listing")    
]   