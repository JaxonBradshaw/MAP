from django.urls import path
from .views import indexPageView, joblistingPageView, joblistingdetailsPageView, editjoblistingPageView, registerJobListingView

urlpatterns = [
    path("", indexPageView, name="landing"),
    path("joblisting/", joblistingPageView, name="job_listing"),
    path("joblistingdetails/<int:joblistingID>/", joblistingdetailsPageView, name="job_listing_details"),
    path("editjoblisting/<int:joblistingID>/", editjoblistingPageView, name="edit_job_listing"),
    path("register/job_listing/", registerJobListingView, name='register_job_listing')
]   