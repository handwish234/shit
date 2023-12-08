# models.py
from django.db import models
 
class Test(models.Model):
    name = models.CharField(max_length=20)

class LoginParams(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    autoLogin = models.BooleanField()
    type = models.CharField(max_length=100)