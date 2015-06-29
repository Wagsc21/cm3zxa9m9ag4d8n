from django.db import models

# Create your models here.
from django.contrib import admin
from django.contrib.auth import settings

# model for options for a dialog 
class Options(models.Model):
    optionID=models.IntegerField(primary_key=True)
    option_text=models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.option_text
    class Meta:
        ordering=['optionID']


"""class CustomManagerForConversation(models.Manager):
    def values_list(self,flat=True):
        return self.values_list(conversationID)
    """
    
# model for conversation
class Conversations(models.Model):
    conversationID=models.IntegerField()
    dialog=models.IntegerField('dialog ID',primary_key=True)
    dialog_text=models.TextField()
    user_conversation=models.ManyToManyField(settings.AUTH_USER_MODEL,through='Userconversation')
    option=models.ManyToManyField(Options,through='Conversationoption',through_fields=('current_conversation','option'))
    
    objects=models.Manager()
    #customobjects=models.CustomManagerForConversation()
    
    def __str__(self):
        return "conversation"+str(self.conversationID)+": "+self.dialog_text
    class Meta:
        ordering=['dialog']



# intermediate model between Users model and Conversation model
# purpose is to store conversation history
class Userconversation(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    conversation=models.ForeignKey(Conversations)
    conversationID=models.IntegerField()
    option_selected=models.ForeignKey(Options)
    conversation_time=models.DateTimeField()
    def __str__(self):
        return str(self.user)+" "+str(self.conversation_time)
    class Meta:
        ordering=['-conversation_time','user']



# intermediate model between Conversations model and Options model
class Conversationoption(models.Model):
    current_conversation=models.ForeignKey(Conversations)
    option=models.ForeignKey(Options)
    next_conversation=models.ForeignKey(Conversations,related_name='next_conversation',null=True,blank=True)
    
    def __str__(self):
        return str(self.current_conversation.dialog)+"-"+str(self. option.optionID)+"-"+str(self.next_conversation.dialog)
    class meta:
        ordering=['current_conversation']
        


