from django.db import models
from django.conf import settings
# Create your models here.

class Challenge(models.Model):
    title = models.CharField(max_length=20)
    problem = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_today = models.BooleanField(default=False)
    rank = models.CharField(max_length=5)
