from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)  # unique teacher ID
    password = models.CharField(max_length=128)

    class Meta:
        db_table = 'teacher'