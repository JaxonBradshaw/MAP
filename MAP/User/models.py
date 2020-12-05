from django.db import models
# Create your models here.

class Organization(models.Model):
    organization_name = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    state_id = models.ForeignKey(State)
    email = models.EmailField(max_length=40)
    size = models.CharField(max_length=20)
    sector = models.CharField(max_length=20)

    def __str__ (self):
        return self.organization_name
class Organization_Admin(Person):
    title = models.CharField(max_length=20)
    organization_id = models.ForeignKey(Organization)

    def __str__ (self):
        pass
