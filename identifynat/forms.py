from .models import *
from django.forms import ModelForm

class Identifynatform(ModelForm):
    class Meta:
        model=IdentifyNat
        exclude=['user']
    #----------------------------------------------------------------------
    def save(self,request,commit=True):
        userform=super(ModelForm,self).save(commit=False)
        userform.user=request.user
        if commit:
            userform.save()
            return userform