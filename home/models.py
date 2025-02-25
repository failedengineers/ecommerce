from django.db import models
from django.utils import timezone
from django.utils.timezone import now


# Create your models here.

class contactus(models.Model):
    email = models.EmailField(max_length=100, null=True, blank=True)

    name = models.CharField(max_length=40)
    number = models.CharField(max_length=12, null=True, blank=True)
    project = models.CharField(max_length=255, null=True, blank=True)
    query_description = models.TextField(null=True, blank=True)
    date=models.DateTimeField(default=now)
    
    def __str__(self):
        
        return self.name 
