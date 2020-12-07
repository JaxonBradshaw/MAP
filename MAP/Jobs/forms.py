from django import forms
from .models import Job_Listing, State, Organization, Organization_Admin


class JobListingForm(forms.form):
    city = forms.CharField(max_length=30)
    state_id = forms.ModelChoiceField(queryset=State.objects.all())
    job_title = forms.CharField(max_length=20)
    org_admin_id = forms.ModelChoiceField(queryset=Organization_Admin.objects.all())
    contracts = forms.CharField(max_length=30)
    description = forms.CharField(max_length=30)
    skills = forms.CharField(max_length=30)
    total_skills = forms.IntegerField()
    skill_value_rating = forms.IntegerField()
    external_app_link = forms.CharField(max_length=50, null=True, blank=True)
    organization_id = forms.ModelChoiceField(queryset=Organization.objects.all())

