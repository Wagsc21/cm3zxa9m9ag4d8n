from django.db import models
from django .contrib.auth import settings
# Create your models here.
class ModifyingBelief(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    description=models.TextField()
    belief=models.TextField()
    technique_used=models.TextField()
    adaptive_belief=models.TextField()
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.user)