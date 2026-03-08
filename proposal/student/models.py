from django.db import models

# Create your models here.
class Proposal(models.Model):
    roll_no = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    file_url = models.URLField(max_length=500)
    feedback = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')