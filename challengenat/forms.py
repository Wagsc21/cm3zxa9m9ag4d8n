from .models import *
from django.forms import ModelForm
"""
this is the form which uses ModelForm to present fields of the model defined in the Meta class model variable
it includes all the fields of model ChallengeNat except the fields mentioned in the exclude set
"""
class Challengenatform(ModelForm):
    class Meta:
        model=ChallengeNat
        exclude=['user']
    #----------------------------------------------------------------------
    def save(self,request,commit=True):
        userform=super(ModelForm,self).save(commit=False)
        userform.user=request.user
        if commit:
            userform.save()
            return userform