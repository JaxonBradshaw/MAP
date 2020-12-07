from django.db import models
from User.models import Organization, State, Organization_Admin, Applicant
# Create your models here.

<<<<<<< HEAD
class Job_Application (models.Model):
    #figure out where to upload to
    resume = models.FileField(upload_to='Resumes')
    citizen = models.IntegerField()
    authorized = models.IntegerField()
    felony = models.IntegerField()
    felony_desc = models.CharField(max_length=30)
    start_date = models.DateField()
    orgization_id = models.OneToOneField("Organization", on_delete=models.CASCADE)
    applicant_id = models.OneToOneField("Applicant", on_delete=models.CASCADE)
    job_listing_id = models.OneToOneField("Job Listing", on_delete=models.CASCADE)

    def __str__(self):
        pass

=======
>>>>>>> cdceb8b7c63b974744d2e49452a0530d3b83e165
class Job_Listing (models.Model):
    city = models.CharField(max_length=30)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=20)
    org_admin_id = models.ForeignKey(Organization_Admin, on_delete=models.CASCADE)
    contracts = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    skills = models.CharField(max_length=30)
    total_skills = models.IntegerField()
    skill_value_rating = models.IntegerField()
    external_app_link = models.URLField(max_length=50)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        pass

class Job_Application (models.Model):
    #figure out where to upload to
    resume = models.FileField(upload_to='Resumes')
    citizen = models.IntegerField()
    authorized = models.IntegerField()
    felony = models.IntegerField()
    felony_desc = models.CharField(max_length=30)
    start_date = models.DateField()
    orgization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job_listing_id = models.ForeignKey(Job_Listing, on_delete=models.CASCADE)

    def __str__(self):
        pass

class Job_Offer (models.Model):
    city = models.CharField(max_length=30)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=30)
    contracts = models.CharField(max_length=30)
    matching_skills = models.IntegerField()
<<<<<<< HEAD
    organization_id = models.OneToOneField("Organization", on_delete=models.CASCADE)
    applicant_id = models.OneToOneField("Applicant", on_delete=models.CASCADE)
    job_listing_id = models.OneToOneField("Job Listing", on_delete=models.CASCADE)
=======
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job_listing_id = models.ForeignKey(Job_Listing, on_delete=models.CASCADE)
>>>>>>> cdceb8b7c63b974744d2e49452a0530d3b83e165
    total_skills = models.IntegerField()

    def __str__(self):
        pass



    