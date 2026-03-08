from django.db import models

# Create your models here.
class Register(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=20)
    program = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    phone_no = models.DecimalField(max_digits=15, decimal_places=0)  
    password = models.CharField(max_length=128)  