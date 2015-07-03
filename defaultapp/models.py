
from django.db import models
from conversationmanager.models import Conversation
from cbt2.models import *
from exercise.models import *
from conversationmanager.models import *
from django.contrib.auth import settings

class Technique(models.Model):
    technique_id=models.IntegerField(primary_key=True)
    module_number=models.IntegerField()
    technique_text=models.CharField(max_length=255,null=True)
    
    #----------------------------------------------------------------------
    def __str__(self):
        return self.technique_text
    class Meta:
        unique_together = ("module_number","technique_text")
        


class DefaultConversation(models.Model):
    technique=models.ForeignKey(Technique)
    conversationID=models.ForeignKey(Conversation)
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.technique)
    
    class Meta:
        ordering=['technique']

"""
class IntermediatebeliefConversation(models.Model):
    technique=models.ForeignKey(Technique)
    conversationID=models.ForeignKey(Conversation)
    intermediatebelief=models.ForeignKey(Intermediatebelief)
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.technique)
        

class CorebeliefConversation(models.Model):
    technique=models.ForeignKey(Technique)
    conversationID=models.ForeignKey(Conversation)
    corebelief=models.ForeignKey(Corebelief)
#----------------------------------------------------------------------
    def __str__(self):
        return str(self.technique)

class PersistentnatConversation(models.Model):
    technique=models.ForeignKey(Technique)
    conversationID=models.ForeignKey(Conversation)
    persistentnat=models.ForeignKey(Persistentnat)
#----------------------------------------------------------------------
    def __str__(self):
        return str(self.technique)
    
class EventlistConversation(models.Model):
    technique=models.ForeignKey(Technique)
    conversationID=models.ForeignKey(Conversation)
    eventlist=models.ForeignKey(Eventlist)
#----------------------------------------------------------------------
    def __str__(self):
        return str(self.technique)    
"""
class ShowTechniqueBeliefsEventsNats(models.Model):
    technique=models.ForeignKey(Technique)
    beliefseventsnats=models.ForeignKey(BeliefsEventsNats)
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.technique)+" "+str(self.beliefseventsnats)
    class Meta:
        unique_together=("technique","beliefseventsnats")
        

class ConversationTechniqueBeliefsEventsNats(models.Model):
    technique=models.ForeignKey(Technique)
    beliefseventsnats=models.ForeignKey(BeliefsEventsNats)
    conversation=models.OneToOneField(Conversation)
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.technique)+" "+str(self.beliefseventsnats)
    
    class Meta:
        unique_together=("technique","beliefseventsnats","conversation")
        
        


class UserConversationTechnique(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    technique=models.ForeignKey(Technique)
    conversation=models.ForeignKey(Conversation)
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.user)+" "+str(self.technique)
    class Meta:
        unique_together=("user","technique","conversation")
        
        
    
class ShownListToUser(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    technique=models.ForeignKey(Technique)
    status=models.BooleanField(default=False)
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.user)
    class Meta:
        unique_together=("user","technique")
        
