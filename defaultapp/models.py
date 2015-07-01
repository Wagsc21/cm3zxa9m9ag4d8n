from django.db import models
from conversationmanager.models import Conversation
from cbt2.models import *
from exercise.models import *
from conversationmanager.models import *
class DefaultConversation(models.Model):
    module_number=models.IntegerField()
    technique=models.CharField(max_length=255,null=True)
    conversationID=models.ForeignKey(Conversation)
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.module_number)+" "+self.technique
    
    class Meta:
        ordering=['module_number','technique']
  
class IntermediatebeliefConversation(models.Model):
    module_number=models.IntegerField()
    technique=models.CharField(max_length=255,null=True)
    conversationID=models.ForeignKey(Conversation)
    intermediatebelief=models.ForeignKey(Intermediatebelief)
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.module_number)+" "+self.technique
        

class CorebeliefConversation(models.Model):
    module_number=models.IntegerField()
    technique=models.CharField(max_length=255,null=True)
    conversationID=models.ForeignKey(Conversation)
    corebelief=models.ForeignKey(Corebelief)
#----------------------------------------------------------------------
    def __str__(self):
        return str(self.module_number)+" "+self.technique    

class PersistentnatConversation(models.Model):
    module_number=models.IntegerField()
    technique=models.CharField(max_length=255,null=True)
    conversationID=models.ForeignKey(Conversation)
    persistentnat=models.ForeignKey(Persistentnat)
#----------------------------------------------------------------------
    def __str__(self):
        return str(self.module_number)+" "+self.technique  
    
class EventlistConversation(models.Model):
    module_number=models.IntegerField()
    technique=models.CharField(max_length=255,null=True)
    conversationID=models.ForeignKey(Conversation)
    eventlist=models.ForeignKey(Eventlist)
#----------------------------------------------------------------------
    def __str__(self):
        return str(self.module_number)+" "+self.technique    
