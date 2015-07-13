from django.db import models
from django.contrib.auth import settings
"""
this model is used in the identifying nat exercise
it has 4 fields:
user: to link a perticular data set with a user
"""
class IdentifyNat(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    situation=models.TextField()
    technique=models.TextField()
    nat=models.TextField()
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.user)