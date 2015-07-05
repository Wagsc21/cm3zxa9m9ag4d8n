from django.db import models

# Create your models here.
from django.contrib import admin
from django.contrib.auth import settings

class Conversation(models.Model):
    conversationID=models.IntegerField(primary_key=True)
        
        #----------------------------------------------------------------------
    def __str__(self):
        return str(self.conversationID)
    class Meta:
        ordering=['conversationID']
        


# model for options for a dialog 
class Options(models.Model):
    optionID=models.IntegerField(primary_key=True)
    option_text=models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.option_text
    class Meta:
        ordering=['optionID']


    
# model for conversation
class Dialogs(models.Model):
    conversationID=models.ForeignKey(Conversation)
    dialog=models.IntegerField('dialog ID',primary_key=True)
    dialog_text=models.TextField()
    #user_conversation=models.ManyToManyField(settings.AUTH_USER_MODEL,through='Userconversation')
    option=models.ManyToManyField(Options,through='Conversationoptiongraph',through_fields=('current_dialog','option'))
    
    objects=models.Manager()
    #customobjects=models.CustomManagerForConversation()
    
    def __str__(self):
        return "conversation"+str(self.conversationID)+": "+self.dialog_text
    class Meta:
        ordering=['dialog']


"""
# intermediate model between Users model and Conversation model
# purpose is to store conversation history
class Userconversation(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    dialog=models.ForeignKey(Dialogs)
    conversationID=models.ForeignKey(Conversation)
    option_selected=models.ForeignKey(Options)
    conversation_time=models.DateTimeField()
    def __str__(self):
        return str(self.user)+" "+str(self.conversation_time)
    class Meta:
        ordering=['-conversation_time','user']

"""

# intermediate model between Conversations model and Options model
class Conversationoptiongraph(models.Model):
    current_dialog=models.ForeignKey(Dialogs)
    option=models.ForeignKey(Options)
    next_dialog=models.ForeignKey(Dialogs,related_name='next_conversation',null=True,blank=True)
    
    def __str__(self):
        return str(self.current_dialog.dialog)+"-"+str(self. option.optionID)+"-"+str(self.next_dialog.dialog)
    class meta:
        ordering=['current_conversation']
        


class ConversationHistory(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    conversationID=models.ForeignKey(Conversation)
    history=models.TextField()
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.user)
        
