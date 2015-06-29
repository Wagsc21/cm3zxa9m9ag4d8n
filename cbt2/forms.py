from django import forms

#"""
from . import models 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from cbt2.customvalidators import validate_email_unique
from django.utils.crypto import get_random_string
from django.conf import settings

CHOICES=[ 
    ('1','just recieve e-mail update'),
    ('2','email update and view profile'),
    ('3','email update,view profile and forum update') 
 ]

GENDER_CHOICES=[
    ('female','FEMALE'),
    ('male','FEMALE'),
    ('other','OTHER'),

]   
def random_uid():                                                                           #to generate random userids
    unique_id=get_random_string(length=25)
    return unique_id


class signupform(UserCreationForm):
    email = forms.EmailField(required=True,validators=[validate_email_unique])
    class Meta:
        model = User
        fields = ('username','email','password1','password2',)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user 


class userdetails(forms.ModelForm):
    ph=forms.CharField(max_length=10, min_length=10)
    
    class Meta:
        model=models.Customuserprofile
        exclude=['user','avatar','phonenumber']
        #fields='__all__'
        widgets={
            #'gender':forms.ChoiceField(),
        }
        #def save(self,uid,commit=True):
#"""
class familydetails(forms.ModelForm):
    ph=forms.CharField(max_length=10, min_length=10)
    class Meta:
        model=models.Familymembers
        exclude=['user','involvementid','phonenumber']
           

class involvement(forms.Form):
   
    involvement=forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES)