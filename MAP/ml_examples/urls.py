from django.urls import path
from .views import dreamJobView, viewDreamJobView

urlpatterns = [
    path("", dreamJobView, name="dream_job"),
    path('viewdreamjob/', viewDreamJobView, name='view_dream_job')  
] 