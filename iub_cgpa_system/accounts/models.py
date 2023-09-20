from django.db import models


# Create your models here.
class my_store(models.Model):
    my_name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
