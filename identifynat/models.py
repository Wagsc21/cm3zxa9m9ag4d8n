from django.db import models
from django.contrib.auth import settings
# Create your models here.
class IdentifyNat(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    situation=models.TextField()
    technique=models.TextField()
    nat=models.TextField()
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.user)