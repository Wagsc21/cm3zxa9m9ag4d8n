
from django.db import models
from defaultapp.models import Technique
"""
ExerciseConversation model is used to store all the conversations related with the exercise 
it has 3 fields:
conversationID is the primary key
conversation_text is the converstion
conversation_type is to denote if it's a base conversation or a technique
"""
from django.conf import settings
class ExerciseConversation(models.Model):
    conversationID=models.IntegerField(primary_key=True)
    conversation_text=models.TextField()
    conversation_type=models.CharField(max_length=255,default='Base')
    def __str__(self):
        return str(self.conversationID)
    class Meta:
        ordering=['conversationID']
        
    
"""
this model store the relation between the base conversation and techniqe converation.
the purpose of this model is to store the possible outcomes of a base conversation.
the techniqe field is a foreign key from the model Defaltapp.models this is included to show to which technique the technique conversation belongs
"""
class ConversationToConversation(models.Model):
    base_conversation=models.ForeignKey(ExerciseConversation,null=True,related_name='base_conversation')
    technique=models.ForeignKey(Technique)
    technique_conversation=models.ForeignKey(ExerciseConversation,null=True,related_name='technique_conversation')
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.base_conversation)+".-- "+str(self.technique)
    class Meta:
        unique_together =("base_conversation","technique")
        
        
"""
this model stores which exercise is to for which model.
it also stores which is/are the correct answer(s) for the exercise
"""
class ConversationToModule(models.Model):
    module_number=models.IntegerField()
    conversationID=models.ForeignKey(ExerciseConversation,null=True,related_name='conversation')
    correct_technique=models.ForeignKey(Technique)
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.module_number) +"--"+ str(self.conversationID) 
  
