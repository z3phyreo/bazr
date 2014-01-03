from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    id_verified = models.BooleanField('ID Verification Status',default=False)
    addr_street = models.CharField('Street Address', max_length=200,blank=True)
    addr_state = models.CharField('State/Province', max_length=200,blank=True)
    addr_zip = models.CharField('Zip Code', max_length=30,blank=True)
    addr_country = models.CharField('Country', max_length=30,blank=True)
    time_zone = models.CharField('Time Zone', max_length=30,blank=True)
    phone = models.CharField('Phone Number', max_length=30,blank=True)
    #joined = models.DateTimeField('Joined', auto_now_add=True,blank=True)


