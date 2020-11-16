from django.db import models

from .choice import *

# Create your models here.
class Vendor(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email1 = models.EmailField()
    email2 = models.EmailField()
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    company_name = models.CharField(max_length=250)
    mobile_number = models.IntegerField()
    telephone_number = models.IntegerField()
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250)
    city = models.CharField(max_length= 100)
    postal_zip = models.IntegerField()
    country = models.IntegerField(choices=COUNTRY)
    state = models.CharField(max_length=100)

    def __str__(self):
        return str(self.first_name)

class Bidder(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email1 = models.EmailField()
    email2 = models.EmailField()
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.first_name)