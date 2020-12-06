from django.urls import path
from .views import indexPageView, choiceView, register_applicantView, register_org_adminView

urlpatterns = [
    path("", indexPageView, name="landing"),
    path("register/", choiceView, name="register"),
    path("register/applicant", register_applicantView, name="register_applicant"),
    path("register/orgadmin", register_org_adminView, name="register_org_admin"),   
]   