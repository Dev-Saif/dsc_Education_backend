from django.db import models

# Create your models here.

class Login(models.Model):

    username = models.CharField(max_length=20,default='Name')
    password = models.CharField(max_length=10,default='Password') 

    def __str__(self):
        return self.username


"""class Account(models.Model):

    name = models.CharField(max_length=20,default='Name')
    password = models.CharField(max_length=10,default='Password') 
"""
