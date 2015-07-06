from django.forms import ModelForm
from .models import *
from datetime import datetime
class UserScheduleForm(ModelForm):
    class Meta:
        model = UserSchedule
        exclude = ['user', 'submit_date']
        
        #----------------------------------------------------------------------
    def save(self,request,commit=True):
        userform=super(ModelForm,self).save(commit=False)
        userform.user=request.user
        userform.submit_date=datetime.now()
        if commit:
            userform.save()
            return userform
            
        
        
    