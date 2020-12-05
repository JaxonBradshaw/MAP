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
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        abstract = True