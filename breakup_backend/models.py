from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    auth_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100) # not necessarily actual name
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    streak_max = models.IntegerField(default=0)
    streak_starts =models.JSONField(default=list) # list of dictionaries.  Keys are strings of dates, values are integers of streaks
    support_info = models.JSONField(default=dict) # dictionary of support info
    struggles_info = models.JSONField(default=dict) # dictionary of struggles info, with a list of breakup Dates
# Create your models here.

class MoodTrackerEntry(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    mood_status = models.IntegerField(default=0)
    days_on_streak = models.IntegerField(default=0)
    last_reset = models.CharField()