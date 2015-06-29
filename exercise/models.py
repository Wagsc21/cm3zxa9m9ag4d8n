from django.db import models

# Create your models here.
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
    technique=models.CharField(max_length=255,null=True)
    technique_conversation=models.ForeignKey(ExerciseConversation,null=True,related_name='technique_conversation')
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.base_conversation)+".-- "+self.technique
        
    
class ConversationToModule(models.Model):
    module_number=models.IntegerField()
    conversation=models.ForeignKey(ExerciseConversation,null=True,related_name='conversation')
    correct_technique=models.CharField(max_length=255,null=True)
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.module_number) +"--"+ str(self.conversation) 
        