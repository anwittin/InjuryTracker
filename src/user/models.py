from django.db import models

# Create your models here.
class User(models.Model):
    first_name      = models.CharField(max_length=30)
    last_name       = models.CharField(max_length=30)
    city            = models.CharField(max_length=60)
    state_province  = models.CharField(max_length=30)
    county          = models.CharField(max_length=50)
    
