
from django.db import models
from conversationmanager.models import Conversation
from cbt2.models import *
from exercise.models import *
from conversationmanager.models import *
from django.contrib.auth import settings
"""
this model store techniques that are to be shown in a module.
it has 3 fields:
technique_id:primary key to represent each technique uniquely
module_number: to which module the technique belong
technique_text: the name of the technique
"""
class Technique(models.Model):
    technique_id=models.IntegerField(primary_key=True)
    module_number=models.IntegerField()
    technique_text=models.CharField(max_length=255,null=True)
    
    #----------------------------------------------------------------------
    def __str__(self):
        return self.technique_text
    class Meta:
        unique_together = ("module_number","technique_text")
        

"""
this mode store the default conversation for any technique
"""
class DefaultConversation(models.Model):
    technique=models.ForeignKey(Technique)
    conversationID=models.ForeignKey(Conversation)
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.technique)
    
    class Meta:
        ordering=['technique']

"""
this model store which option outof the list in model BeliefsEventsNats has to be shown in which module
"""
class ShowTechniqueBeliefsEventsNats(models.Model):
    technique=models.ForeignKey(Technique)
    beliefseventsnats=models.ForeignKey(BeliefsEventsNats)
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.technique)+" "+str(self.beliefseventsnats)
    class Meta:
        unique_together=("technique","beliefseventsnats")
        
"""
this model store which conversation should be shown to a user in which module if he selects a perticular item from the list.
this technique stores relation betwwen BeliefsEventsNats, Technique, Conversation
"""
class ConversationTechniqueBeliefsEventsNats(models.Model):
    technique=models.ForeignKey(Technique)
    beliefseventsnats=models.ForeignKey(BeliefsEventsNats)
    conversation=models.OneToOneField(Conversation)
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.technique)+" "+str(self.beliefseventsnats)
    
    class Meta:
        unique_together=("technique","beliefseventsnats","conversation")
        
        

"""
once it is determined what options are selected by user we add the corrosponding conversation for the technique to which it belong for the user
"""
class UserConversationTechnique(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    technique=models.ForeignKey(Technique)
    conversation=models.ForeignKey(Conversation)
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.user)+" "+str(self.technique)
    class Meta:
        unique_together=("user","technique","conversation")
        
        
"""
this model stores that for a technique if list of options is shown or not if yes we set status= True
"""
class ShownListToUser(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    technique=models.ForeignKey(Technique)
    status=models.BooleanField(default=False)
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.user)
    class Meta:
        unique_together=("user","technique")
        
