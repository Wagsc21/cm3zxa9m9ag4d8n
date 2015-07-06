from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# model Users for user registration details
from django.conf import settings
GENDER_CHOICES=(
    ('female','FEMALE'),
    ('male','MALE'),
    ('other','OTHER'),

 )
CATEGORY_CHOICES=(
    ('corebelief','Corebelief'),
    ('intermediatebelief','Intermediatebelief'),
    ('persistentnat','PersistentNAT'),
    ("event","Event"),

)
"""
NOTE- setting.AUTH_USER_MODEL is a name used for django.contrib.auth.models.User (https://docs.djangoproject.com/en/1.8/ref/contrib/auth/#user)
model and table are synonyms. model is django keyword and table is for Mysql. i have used model (everywhere) in this commenting
similarly field and column synonyms. field is django keyword and column is for Mysql. i have used field (everywhere) in this commenting
"""

"""
this is a model for storing the occupations list to show to user and let him select one for his profile
it has 2 fields one is primary key(occupationID) and one is for the name of the occupation(eg. busineesman,teacher)
THIS IS FOR ADMIN PURPOSE
"""
class Occupations(models.Model):
    occupationID=models.AutoField(primary_key=True)
    occupation_name=models.CharField(max_length=20,blank=True,null=True)
    def __str__(self):
        return self.occupation_name

# model Countries for storing list of countries
"""
this is a model for storing the list of countries 
ordering is done lexicographically
this model can be altered from django admin site
THIS IS FOR ADMIN PURPOSE
"""

class Countries(models.Model):
    countryID=models.IntegerField(primary_key=True)
    country_Name=models.CharField(max_length=20)
    def __str__(self):
        return self.country_Name
    class Meta:
        ordering=['country_Name']

"""
this is a model for storing avatars and the path to the image file
this model can be altered from django admin site
THIS IS FOR ADMIN PURPOSE TO ADD NEW AVATARS
"""
#model Avatars for storing avatars
class Avatars(models.Model):
    avatarID=models.IntegerField(primary_key=True)
    avatarImage=models.CharField(max_length=255)
    def __str__(self):
        return str(self.avatarID)

"""
this is a model for storing list of education qualification from which user has to choose one
this contains 2 fields one educationID(primary key) and two as the education qualification
this model can be altered from django admin site
THIS IS FOR ADMIN PURPOSE
"""
#model Education for education list
class Education(models.Model):
    educationID=models.IntegerField(primary_key=True)
    education_qualification=models.CharField(max_length=20,blank=True,null=True)
    def __str__(self):
        return self.education_qualification

#model Age for age group
"""
this is a model created for defining different age groups to which user can belong
it has 2 fields: agegroupID is the primarykey for the model and and second field is for defining age range (eg. 20-25)
THIS IS FOR AMDIN PURPOSE
"""
class Age(models.Model):
    agegroupID=models.AutoField(primary_key=True)
    agegroup=models.CharField(max_length=10)
    def __str__(self):
        return self.agegroup
    class Meta:
        ordering=['agegroupID']


# model Test for depression and anxity score
"""
this is a model created two store the depression and anxiety score for user 
this model has 15 fields 1st is a foreign key from the settings.AUTH_USER_MODEL to link the test with a perticular user
and 7 dsasweeki fields for ith (1-7) week's depression score
and 7 asweeki fields for ith (1-7) week's anxiety score
THIS WILL BE UPDATED BY USER AT THE START OF EACH MODULE
"""
class Test(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    dsasweek1=models.CharField(max_length=50,blank=True,null=True)
    dsasweek2=models.CharField(max_length=50,blank=True,null=True)
    dsasweek3=models.CharField(max_length=50,blank=True,null=True)
    dsasweek4=models.CharField(max_length=50,blank=True,null=True)
    dsasweek5=models.CharField(max_length=50,blank=True,null=True)
    dsasweek6=models.CharField(max_length=50,blank=True,null=True)
    dsasweek7=models.CharField(max_length=50,blank=True,null=True)    
    asweek1=models.CharField(max_length=50,blank=True,null=True)
    asweek2=models.CharField(max_length=50,blank=True,null=True)
    asweek3=models.CharField(max_length=50,blank=True,null=True)
    asweek4=models.CharField(max_length=50,blank=True,null=True)
    asweek5=models.CharField(max_length=50,blank=True,null=True)
    asweek6=models.CharField(max_length=50,blank=True,null=True)
    asweek7=models.CharField(max_length=50,blank=True,null=True)
    
    def __str__(self):
        return str(self.user)

    
# model UserProfile for storing user's complete profile
"""
this is the model to store user's details it has 8 fields
user: OneToOne relation with settings.AUTH_USER_MODEL to link a record to a single user
agegroup,education,country,erolled_asand avatar as foreign key from model Age,Education,Countries,Occupation,Avatar
gender field can have only 3 possible choices defined in GENDER_CHOICES to add more choices add the choice to tuple set GENDER_CHOICES
phonenumber is to store phonenumber (^_^)
THIS WILL BE UPDATED BY USER
"""
class Customuserprofile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL)
    agegroup=models.ForeignKey(Age)
    education=models.ForeignKey(Education)
    country=models.ForeignKey(Countries)
    enrolled_as=models.ForeignKey(Occupations)
    avatar=models.ForeignKey(Avatars,default=1)
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    phonenumber=models.CharField(max_length=10)
    def __str__(self):
        return str(self.user)


"""
this is model to store family member details of the user if user involves one(many)
to link a family member to a user model has a field as a foreing key from settings.AUTH_USER_MODEL
and rest fields are for the details of the family member
THIS WILL BE UPDATED BY USER IF HE /SHE INVOLVE A FAMILY MEMBER
"""
class Familymembers(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    member_name=models.CharField('Name',max_length=200)
    relate=models.CharField('Relation to you',max_length=50,default='')
    emailid=models.EmailField('Email ID',max_length=25,blank=True,null=True)
    phonenumber=models.CharField('Phone Number',max_length=10,blank=True,null=True)
    involvementid=models.IntegerField(default=0)
    def __str__(self):
        return str(self.user)


# model Corebelief for list of corebeliefs , intermediatebelief , persistent nat, and event
"""
this model stores list of all corebeliefs, Intermediatebeliefs, Persistent NATS and Events 
it has 3 fields :
1st: beliefseventsnatsID as primarykey 
2nd: beliefseventsnatsID , the text 
3rd: category value for one row can only be one of CATEGORY_CHOICES
THIS IS FOR ADMIN PURPOSE TO UPDATE THE LIST USE dbpopulator FILE
"""
class BeliefsEventsNats(models.Model):
    beliefseventsnatsID=models.IntegerField(primary_key=True)
    beliefseventsnats_text=models.TextField()
    category=models.CharField(max_length=25,choices=CATEGORY_CHOICES)
    
    #----------------------------------------------------------------------
    def __str__(self):
        return self.beliefseventsnats_text+"----"+self.category
"""
this is a model used to store user's corebeliefs, Intermediatebeliefs, Persistent NATS and Events 
it has 2 fields:
1st: foreing key from settings.AUTH_USER_MODEL
2nd : foreign key from BeliefsEventsNats
THIS MODEL WILL BE UPDATED BY THE OPTIONS USER SELECTED FROM THE PRESENTED LIST OF COREBELIEFS, INTERMEDIATEBELIEFS, PERSISTENT NATS AND EVENTS  AT THE START OF EACH TECHNIQUE
"""
class UserBeliefsEventsNats(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    beliefs_events_nats=models.ForeignKey(BeliefsEventsNats)
    
    #----------------------------------------------------------------------
    def __str__(self):
        return str(self.user)
    
    class Meta:
        unique_together=("user","beliefs_events_nats")
        
        
