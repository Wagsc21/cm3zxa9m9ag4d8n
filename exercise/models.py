
from django.db import models
from defaultapp.models import Technique
# Create your models here.
from django.conf import settings
class ExerciseConversation(models.Model):
    conversationID=models.IntegerField(primary_key=True)
    conversation_text=models.TextField()
    conversation_type=models.CharField(max_length=255,default='Base')
    def __str__(self):
        return str(self.conversationID)
    class Meta:
        ordering=['conversationID']
        
    
#class Methodsconversation
class ConversationToConversation(models.Model):
    base_conversation=models.ForeignKey(ExerciseConversation,null=True,related_name='base_conversation')
    technique=models.ForeignKey(Technique)
    technique_conversation=models.ForeignKey(ExerciseConversation,null=True,related_name='technique_conversation')
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.base_conversation)+".-- "+str(self.technique)
    class Meta:
        unique_together =("base_conversation","technique")
        
        
    
class ConversationToModule(models.Model):
    module_number=models.IntegerField()
    conversationID=models.ForeignKey(ExerciseConversation,null=True,related_name='conversation')
    correct_technique=models.ForeignKey(Technique)
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.module_number) +"--"+ str(self.conversationID) 
"""
class IdentifyNat(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    situation=models.TextField()
    technique=models.TextField()
    nat=models.TextField()
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.user)
        
    
class ChallengeNat(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    situation=models.TextField()
    nat=models.TextField()
    technique=models.TextField()
    resolution=models.TextField()
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.user)
        
    
class ModifyingBelief(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    description=models.TextField()
    belief=models.TextField()
    technique_used=models.TextField()
    adaptive_belief=models.TextField()
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.user)        
 """  
