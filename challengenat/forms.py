from .models import *
from django.forms import ModelForm

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