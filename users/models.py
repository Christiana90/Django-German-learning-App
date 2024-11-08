from django.db import models


class Register (models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    
    

# Create your models here.
