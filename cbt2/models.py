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
"""
class Customeuser(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL)
    users_account_id=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
    	return str(self.user)
"""
class Occupations(models.Model):
    occupationID=models.AutoField(primary_key=True)
    occupation_name=models.CharField(max_length=20,blank=True,null=True)
    def __str__(self):
        return self.occupation_name

# model Countries for storing list of countries

class Countries(models.Model):
    countryID=models.IntegerField(primary_key=True)
    country_Name=models.CharField(max_length=20)
    def __str__(self):
        return self.country_Name
    class Meta:
        ordering=['country_Name']

#model Avatars for storing avatars
class Avatars(models.Model):
    avatarID=models.IntegerField(primary_key=True)
    avatarImage=models.CharField(max_length=255)
    def __str__(self):
        return str(self.avatarID)


#model Education for education list
class Education(models.Model):
    educationID=models.IntegerField(primary_key=True)
    education_qualification=models.CharField(max_length=20,blank=True,null=True)
    def __str__(self):
        return self.education_qualification

#model Age for age group
class Age(models.Model):
    agegroupID=models.AutoField(primary_key=True)
    agegroup=models.CharField(max_length=10)
    def __str__(self):
        return self.agegroup
    class Meta:
        ordering=['agegroupID']


# model Test for depression and anxity score

class Test(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    dsasweek1=models.CharField(max_length=50,blank=True,null=True)
    dsasweek2=models.CharField(max_length=50,blank=True,null=True)
    dsasweek3=models.CharField(max_length=50,blank=True,null=True)
    dsasweek4=models.CharField(max_length=50,blank=True,null=True)
    dsasweek5=models.CharField(max_length=50,blank=True,null=True)
    asweek1=models.CharField(max_length=50,blank=True,null=True)
    asweek2=models.CharField(max_length=50,blank=True,null=True)
    asweek3=models.CharField(max_length=50,blank=True,null=True)
    asweek4=models.CharField(max_length=50,blank=True,null=True)
    asweek5=models.CharField(max_length=50,blank=True,null=True)    
    
    def __str__(self):
        return str(self.user)

    
# model UserProfile for storing user's complete profile

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
 #"""

class Familymembers(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    member_name=models.CharField('Name',max_length=200)
    relate=models.CharField('Relation to you',max_length=50,default='')
    emailid=models.EmailField('Email ID',max_length=25,blank=True,null=True)
    phonenumber=models.CharField('Phone Number',max_length=10,blank=True,null=True)
    involvementid=models.IntegerField(default=0)
    def __str__(self):
        return str(self.user)


# model Corebelief for lsit of corebeliefs
# custom manager for getting Corebelief instance regarding views/set_list()
class CustomManagerFOrCorebelief(models.Manager):
    def my_queryset(self,val):
        return self.get(corebeliefID=val)

class Corebelief(models.Model):
    corebeliefID=models.IntegerField(primary_key=True)
    corebelief_text=models.TextField()
    corebeliefs=models.ManyToManyField(settings.AUTH_USER_MODEL,through='Userscb')

    objects=models.Manager()
    filtered_objects=CustomManagerFOrCorebelief()            # object of CustomManager for custom query

    def __str__(self):
        return self.corebelief_text
    class Meta:
        ordering=['corebeliefID']




# intermediate model between Users model and Corebelief model
#custom manager for creating a Usercb instance regarding views/set_list()
class CustomManagerForUserscb(models.Manager):
    def customcreate(self,uid,corebelief):
        return self.get_or_create(user=uid,corebelief=corebelief)

class Userscb(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    corebelief=models.ForeignKey(Corebelief)

    objects=models.Manager()
    filtered_objects=CustomManagerForUserscb()

    def __str__(self):
        return str(self.user)




# model Intermediatebelief list of intermediate beliefs
# custom manager for getting Intermediatebelief instance regarding views/set_list()
class CustomManagerFOrIntermediatebelief(models.Manager):
    def my_queryset(self,val):
        return self.get(intermediatebeliefID=val)

class Intermediatebelief(models.Model):
    intermediatebeliefID=models.IntegerField(primary_key=True)
    intermediatebelief_text=models.TextField()
    intermediatebeliefs=models.ManyToManyField(settings.AUTH_USER_MODEL,through='Usersib')

    objects=models.Manager()
    filtered_objects=CustomManagerFOrIntermediatebelief()    
    def __str__(self):
        return self.intermediatebelief_text
    class Meta:
        ordering=['intermediatebeliefID']   

# intermediate model between Users model and Intermediatebelief model
#custom manager for creating aUsersib instance regarding views/set_list()
class CustomManagerForUsersib(models.Manager):
    def customcreate(self,uid,intermediatebelief):
        return self.get_or_create(user=uid,intermediatebelief=intermediatebelief)

class Usersib(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    intermediatebelief=models.ForeignKey(Intermediatebelief)

    objects=models.Manager()
    filtered_objects=CustomManagerForUsersib()

    def __str__(self):
        return str(self.user)

#model Persistentnet for list of persistent NATS
# custom manager for getting Persistentnat instance regarding views/set_list()
class CustomManagerFOrPersistentnat(models.Manager):
    def my_queryset(self,val):
        return self.get(persistentnatID=val)

class Persistentnat(models.Model):
    persistentnatID=models.IntegerField(primary_key=True)
    persistentnat_text=models.TextField()
    persistentnats=models.ManyToManyField(settings.AUTH_USER_MODEL,through='Userpnat')

    objects=models.Manager()
    filtered_objects=CustomManagerFOrPersistentnat()    
    def __str__(self):
        return self.persistentnat_text
    class Meta:
        ordering=['persistentnatID']

# intermediate model between Users and Persistentnet model
#custom manager for creating a Userpnat instance regarding views/set_list()
class CustomManagerForUserpnat(models.Manager):
    def customcreate(self,uid,persistentnat):
        return self.get_or_create(user=uid,persistentnat=persistentnat)

class Userpnat(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    persistentnat=models.ForeignKey(Persistentnat)

    objects=models.Manager()
    filtered_objects=CustomManagerForUserpnat()

    def __str__(self):
        return str(self.user)
    

# model for list of events
# custom manager for getting Eventlist instance regarding views/set_list()
class CustomManagerFOrEvent(models.Manager):
    def my_queryset(self,val):
        return self.get(eventID=val)

class Eventlist(models.Model):
    eventID=models.IntegerField(primary_key=True)
    event_text=models.TextField()
    event=models.ManyToManyField(settings.AUTH_USER_MODEL,through='Userevent')

    objects=models.Manager()
    filtered_objects=CustomManagerFOrEvent()    
    def __str__(self):
        return self.event_text
    class Meta:
        ordering=['eventID']

# intermediate model between Users model and Eventlist model
#custom manager for creating a Userevent instance regarding views/set_list()
class CustomManagerForUserevent(models.Manager):
    def customcreate(self,uid,event):
        return self.get_or_create(user=uid,event=event)

class Userevent(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    event=models.ForeignKey(Eventlist)
    chaeck=models.BooleanField(default=False)

    objects=models.Manager()
    filtered_objects=CustomManagerForUserevent()

    def __str__(self):
        return str(self.user)