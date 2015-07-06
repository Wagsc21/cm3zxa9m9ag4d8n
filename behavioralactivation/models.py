from django.db import models
from django.contrib.auth import settings

class UserSchedule(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)    
    sleeping = models.IntegerField(default=0)
    mastery = models.IntegerField(default=0)
    pleasure = models.IntegerField(default=0)
    rumination = models.IntegerField(default=0)
    distractionAndAvoidance = models.IntegerField(default=0)
    miscellaneous = models.IntegerField(default=0)
    submit_date=models.DateTimeField()
    
    def __str__(self):
        return str(self.user)
