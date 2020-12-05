from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class State(models.Model) :
    state_name = models.CharField(max_length=20)
    state_abbrev = models.CharField(max_length =2)

    def __str__ (self) :
        return(self.state_name)

class Ethnicity(models.Model) :
    ethnicity_name = models.CharField(max_length=30)

    def __str__ (self) :
        return(self.ethnicity_name)

class Person (User) :
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    zip = models.CharField(max_length=5)
    state_id = models.OneToOneField("State", on_delete=models.SET_NULL)
    ethnicity = models.OneToOneField("Ethnicity", on_delete=models.SET_NULL)

    class Meta:
        proxy = True

class Organization(models.Model):
    organization_name = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    state_id = models.OneToOneField(State, on_delete=models.SET_NULL)
    email = models.EmailField(max_length=40)
    size = models.CharField(max_length=20)
    sector = models.CharField(max_length=20)

    def __str__ (self):
        return self.organization_name
class Organization_Admin(Person):
    title = models.CharField(max_length=20)
    organization_id = models.OneToOneField(Organization, on_delete=models.SET_NULL)

    def __str__ (self):
        return(self.first_name + '' + self.last_name)
