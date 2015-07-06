from django.db import models
from django.contrib.auth import settings

"""
NOTE: setting.AUTH_USER_MODEL is name used for django.contrib.auth.User
"""
"""
this model is used for storing user's schedule along with the time and date stamp. 
this model has a foreign key from setting.AUTH_USER_MODEL to link it with a user. 
for every week a new row will be created for the user.
it is supposed to be filled after an interval of 7 days.
"""
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
