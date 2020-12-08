from django import forms
from .models import Job_Listing, State, Organization, Organization_Admin

SKILLS = {
    ('django', 'Django'),
    ('python', 'Python'),
    ('html', 'HTML'),
    ('iphone', 'iPhone'),
    ('excel', 'Excel')
}
class JobListingForm(forms.Form):
    city = forms.CharField(max_length=30)
    state_id = forms.ModelChoiceField(queryset=State.objects.all())
    job_title = forms.CharField(max_length=20)
    org_admin_id = forms.ModelChoiceField(queryset=Organization_Admin.objects.all())
    contracts = forms.CharField(max_length=30)
    description = forms.CharField(max_length=30)
    skills = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SKILLS)
    total_skills = forms.IntegerField()
    skill_value_rating = forms.IntegerField()
    external_app_link = forms.CharField(max_length=50)
    organization_id = forms.ModelChoiceField(queryset=Organization.objects.all())

    class Meta:
        model = Job_Listing
        fields = ['city', 'state_id', 'job_title', 'org_admin_id', 'contracts', 'description', 'skills', 'total_skills', 'skill_value_rating', 'organization_id']
