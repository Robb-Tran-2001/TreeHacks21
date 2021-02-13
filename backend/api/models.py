from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(null=False, default=0, unique=True, primary_key=True)
    username=models.CharField(max_length=30, default="", unique=True)
    password=models.CharField(max_length=30, default="", unique=True)


