from django.db import models
from django.contrib import admin
from django.contrib.auth import settings

"""
this model has a single field. this model is used everywhere as a foreign key to associate dialogs to a 
perticular conversation
"""
class Conversation(models.Model):
    conversationID=models.IntegerField(primary_key=True)
        
        #----------------------------------------------------------------------
    def __str__(self):
        return str(self.conversationID)
    class Meta:
        ordering=['conversationID']
        


"""
this model is used to store the options.
"""
class Options(models.Model):
    optionID=models.IntegerField(primary_key=True)
    option_text=models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.option_text
    class Meta:
        ordering=['optionID']


    
"""
this model stores the dialog which will be used by the automated system for conversation
it has a foreignkey field to link the dialogs with a conversation.
dialogs with same conversationID field are part of same conversation
"""
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
this model store the graph between the dialogs as a triplet (current_dialog-option-next_dialog)
to carry out a conversation we match for current_dialog and option and determine system's next dialog
"""
class Conversationoptiongraph(models.Model):
    current_dialog=models.ForeignKey(Dialogs)
    option=models.ForeignKey(Options)
    next_dialog=models.ForeignKey(Dialogs,related_name='next_conversation',null=True,blank=True)
    wrong_option=models.BooleanField(default=False)
    def __str__(self):
        return str(self.current_dialog.dialog)+"-"+str(self. option.optionID)+"-"+str(self.next_dialog.dialog)
    class meta:
        ordering=['current_conversation']
        
"""
this model store history for every user.
only latest history is stored for any conversation.
the history is stored as a single string
"""
class ConversationHistory(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    conversationID=models.ForeignKey(Conversation)
    history=models.TextField()
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.user)
        
