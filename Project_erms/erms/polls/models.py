from django.db import models

# Create your models here.
class InfoBasic(models.Model):
    First_name       = models.CharField(max_length=50)
    Last_name  = models.CharField(max_length=50)
    Age    = models.IntegerField()
    Email = models.EmailField()
    Gender = models.CharField(max_length=50),
