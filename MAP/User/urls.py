from django.urls import path
from .views import indexPageView, choiceView, register_applicantView, register_org_adminView, profileView
from .views import viewApplicantsView, viewOrgAdminView, dreamJobView, viewDreamJobView

urlpatterns = [
    path("", indexPageView, name="landing"),
    path("register/", choiceView, name="register"),
    path("register/applicant", register_applicantView, name="register_applicant"),
    path("register/orgadmin", register_org_adminView, name="register_org_admin"), 
    path('profile/', profileView, name='profile'),
    path('applicants/', viewApplicantsView, name='applicants'),
    path('organizationadmin/', viewOrgAdminView, name='orgadmin'),
    path('dreamjob/', dreamJobView, name='dream_job'),
    path('viewdreamjob/', viewDreamJobView, name='view_dream_job')  
] 