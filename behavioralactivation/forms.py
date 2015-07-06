from django.forms import ModelForm
from .models import *
from datetime import datetime
"""
this form is created using ModelForm (https://docs.djangoproject.com/en/1.8/topics/forms/modelforms/) to get user's schedule.
it has all fields of model defined in the class Meta model variable.
except  the fields mentioned in the exclude set. Also the super save method is overrided to set the user and datetime stamp and then it is saved.
"""
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
            
        
        
    