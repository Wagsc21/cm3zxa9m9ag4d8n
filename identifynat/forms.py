from .models import *
from django.forms import ModelForm
"""
this form is a ModelForm used the identifying nat exercise.
it has 3 fields (all except the 'user' field of the Model class IdentifyNat)
"""
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