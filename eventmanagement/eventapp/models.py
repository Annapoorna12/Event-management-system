from django.db import models

# Create your models here.
class Event(models.Model):
    event_title = models.CharField(max_length=120)
    location = models.CharField(max_length=70)
    date = models.CharField(max_length=120)
    description = models.TextField()
    