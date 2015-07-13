from django.db import models
from django.contrib.auth import settings
#--------------------------------------------------------------------
"""
NOTE:- settings.AUTH_USER_MODEL is name used for django.contrib.auth.User
this model is used to store the user's experience in the exercises of the module challenge NAT
"""
class ChallengeNat(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    situation=models.TextField()
    nat=models.TextField()
    technique=models.TextField()
    resolution=models.TextField()
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.user)