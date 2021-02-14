from django.db import models

# Models for JSON creation
class User(models.Model):
    username=models.CharField(max_length=20, null=False, unique=True)
    password=models.CharField(max_length=20, null=False)

class Image(models.Model):
    name = models.CharField(blank=True, max_length=255, default='')
    image = models.ImageField(null=True, blank=True)
    hash_con = models.CharField(blank=True,max_length=512, default="")
    hash_div = models.CharField(blank=True,max_length=512, default="")
    hash = models.CharField(blank=True,max_length=512, default="")
    timestamp = models.FloatField(null=True, blank=True)