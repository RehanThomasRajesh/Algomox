# analytics_dashboard/models.py
from django.db import models
from django.contrib.auth.models import User

class SocialMediaData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=20)
    date = models.DateField(null=True)
    followers = models.IntegerField()
    engagements = models.IntegerField()
    impressions = models.IntegerField()

    def __str__(self):
        return f"{self.platform} - {self.date}"
