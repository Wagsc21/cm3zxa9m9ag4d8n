#"""
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render,render_to_response ,redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.core.urlresolvers import reverse
from .forms import * 
from django.core import serializers
from django.views.decorators.cache import cache_control
from django.utils.crypto import get_random_string
from datetime import datetime
from . import models , forms
from django.contrib.auth.decorators import login_required
from django.conf import settings
corebelief_list_size=11
intermediatebelief_list_size=15
persistentnat_list_size=16
event_list_size=15
depression_list=[
    'Have you found little pleasure or interest in doing things?',
    'Have you found yourself feeling down, depressed or hopeless?',
    'Have you had trouble falling asleep, staying asleep or are you sleeping too much?',
    'Have you been feeling tired or had little energy?',
    'Have you had a poor appetite or been overeating?',
    'Have you been feeling worthless, like you have let yourself or your family down?',
    'Have you had trouble concentrating or thinking or feeling very indecisive?',
    'Have you been moving slowly or speaking slowly or been very agitated so that others are able to notice?',
    'Have you been having suicidal thoughts with or without a specific plan or have you been hurting yourself in some way?', 


]

anxiety_list=[
    'Feeling nervous, anxious or on edge',
    'Not being able to stop or control worrying',
    'Worrying too much about different things',
    'Trouble relaxing',
    'Being so restless that it is hard to sit still',
    'Becoming easily annoyed or irritable',
    'Feeling afraid as if something awful might happen',

]
#function to generate random string [not used yet]
def random_uid():
    unique_id=get_random_string(length=25)
    return unique_id


# renders request to home page
def home(request):
    return render(request,'cbt2/home.html')
#----------------------------------------------------------------------
@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request,'cbt2/welcome.html')
def usersignup(request):
    if request.method =='GET':
        form=forms.signupform()
    else:
        form = forms.signupform(request.POST)
        if form.is_valid():
            user=form.save()
            username= user.get_username()
            request.session['username']=username
            #user1=models.Customeuser.objects.create(user=user,users_account_id=uid)
            test1=models.Test.objects.create(user=user)
            args = {}
            args.update(csrf(request))
            return HttpResponseRedirect('/fill/details/')
            
                
            
    return render(request,'cbt2/usersignup.html',{'form':form})

# login function for authentication
def login(request):
    c = {}
    c.update(csrf(request))
    return render(request,'cbt2/login.html') 

# function where actually username and password is authenticated
def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request,user)
        request.session['username']=user.get_username()
        if user.is_superuser:
            return HttpResponseRedirect('/admin_page/')
        return HttpResponseRedirect('/welcome/')
    else:
        return HttpResponseRedirect('/accounts/invalid')

# function that will handel all request after logging in also prevent browser caching of log in page once logout
def loggedin(request):
    if(request.GET['next']==None):
        return HttpResponseRedirect('/home/')
    else:
        return HttpResponseRedirect(request.GET['next'])

# action in case of invalid login details
def invalid_login(request):
    return render(request,'cbt2/invalid_login.html')

@cache_control(no_cache=True, must_revalidate=True)


# function that log out user

def logout(request):
    auth.logout(request)
    return render(request,'cbt2/logout.html')


# function for recording and handelling froms.userdetails form
@login_required(login_url='/accounts/login/')
def user_details(request):
    if request.method == 'GET':
        form=userdetails()
    else:
        form=userdetails(request.POST)
        if form.is_valid():
            username=request.session['username']
            user=User.objects.get(username=username)
            age=form.cleaned_data['agegroup']
            edu=form.cleaned_data['education']
            country=form.cleaned_data['country']
            occu=form.cleaned_data['enrolled_as']
            gen=form.cleaned_data['gender']
            phno=form.cleaned_data['ph']
            done=models.Customuserprofile.objects.create(user=user,agegroup=age,education=edu,country=country,enrolled_as =occu,gender=gen,phonenumber=phno)
            args ={}
            args.update(csrf(request))
            return HttpResponseRedirect('/fill/family_details/')
    return render(request,'cbt2/userinfo.html',{'form': form})
    #"""


# function for recording and handelling forms.familydetails form
@login_required(login_url='/accounts/login/')
def family_details(request):
    if request.method == 'GET':
        form=familydetails()
    else:
        form=familydetails(request.POST)
        if form.is_valid():
            username=request.session['username']
            user=User.objects.get(username=username)
            #request.session['userid']=user
            mname=form.cleaned_data['member_name']
            eid=form.cleaned_data['emailid']
            phno=form.cleaned_data['ph']
            rtou=form.cleaned_data['relate']
            #invoid=form.cleaned_data['involvementid']
            done=models.Familymembers.objects.create(user=user,member_name=mname,emailid=eid,phonenumber=phno,relate=rtou)
            args = {}
            args.update(csrf(request))
            return HttpResponseRedirect("/user/setting/")
    return render(request,'cbt2/userfamilyinfo.html',{'form': form})

# function for taking involvement extent of user family 
@login_required(login_url='/accounts/login/')
def settings(request):
    if request.method == 'GET':
        form=involvement()
    else:
        form=involvement(request.POST)
        if form.is_valid():
            username=request.session['username']
            user=User.objects.get(username=username)
            invo=form.cleaned_data['involvement']
            models.Familymembers.objects.filter(user=user).update(involvementid=invo)
            return HttpResponseRedirect('/depression_quiz/')
    return render(request,'cbt2/setting.html',{'form':form})

#function for recording and handelling user's depression and anxiety quiz
@login_required(login_url='/accounts/login/')
def depression_score(request,num):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    if request.method == 'GET':
        form=request.GET
    elif request.method == 'POST':
        form=request.POST
    username=request.session['username']
    user=User.objects.get(username=username)  
    try:
        q1=0
        q2=''
        stri=''
        if int(num) == 9:
            stri=stri+'depression'
            for i in range (1,int(num)+1):
                h=request.POST.get('depression_question_0%d' %i)
                q1=q1+int(h)
                q2=q2+h
            models.Test.objects.filter(user=user).update(dsasweek1=q2)
            return HttpResponseRedirect('/anxiety_quiz/')
        elif int(num) == 7:
            stri=stri+'anxiety'
            for i in range (1,int(num)+1):
                h=request.POST.get('anxiety_question_0%d' %i)
                q1=q1+int(h)
                q2=q2+h
            models.Test.objects.filter(user=user).update(asweek1=q2)
            return HttpResponseRedirect('/corebeliefs/1')  
                              
        
    except:
        if int(num) == 9:
            return render(request,'cbt2/depression.html',{'error_message': "select one option for each question",'quiz_list':depression_list},)
        elif int(num) == 7:
            return render(request,'cbt2/anxiety.html',{'error_message': "select one option for each question",'quiz_list': anxiety_list},)
            
    else:
        return HttpResponse('<hmtl><body>done for</body></html>')
            
    #"""
    
#function to show any of list given in argument
@login_required(login_url='/accounts/login/')
def show_list(request,sender,reciever,num,list_size):
    try:
        x=list_size*(int(num)-1)
        list=sender.objects.all()[x:x+list_size]
        return render(request,'cbt2/%s.html' %reciever,{'%ss_list' %reciever : list,'num':num})
    except(KeyError):
        return HttpResponse('<html><body>error </body></html>')

#function for recording the choosen options of show list function
@login_required(login_url='/accounts/login/')
def set_list(request,to_set,sender,reciever,num,list_size):
    try:
        username=request.session['username']
        user=User.objects.get(username=username)
        x=list_size*(int(num)-1)
        for i in range(x,x+list_size):
            if not request.POST.get('optionID%d' % (i+1),None) == None:
                r=sender.filtered_objects.my_queryset(i+1)
                to_set.filtered_objects.customcreate(user,r)
        #return HttpResponse(r)
        return HttpResponseRedirect('/%s/%s' %(reciever,num))
    except KeyError as e:
        return HttpResponse('error'+str(e))


@login_required(login_url='/accounts/login/')
def set_corebeliefs(request,num):
    return set_list(request,to_set=models.Userscb,sender=models.Corebelief,reciever='intermediatebeliefs',num=num,list_size=corebelief_list_size)

@login_required(login_url='/accounts/login/')
def show_corebeliefs(request,num):
    global corebelief_list_size
    return show_list(request,sender=models.Corebelief,reciever='corebelief',num=num,list_size = corebelief_list_size)


def show_intermediatebeliefs(request,num):
    global intermediatebelief_list_size
    return show_list(request,sender=models.Intermediatebelief,reciever='intermediatebelief',num=num,list_size = intermediatebelief_list_size)

@login_required(login_url='/accounts/login/')
def show_persistentnats(request,num):
    global persistentnat_list_size
    return show_list(request,sender=models.Persistentnat,reciever='persistentnat',num=num,list_size = persistentnat_list_size)

@login_required(login_url='/accounts/login/')
def show_events(request,num):
    global event_list_size
    return show_list(request,sender=models.Eventlist,reciever='event',num=num,list_size=event_list_size)

@login_required(login_url='/accounts/login/')
def set_intermediatebeliefs(request,num):
    return set_list(request,to_set=models.Usersib,sender=models.Intermediatebelief,reciever='persistentnats',num=num,list_size=intermediatebelief_list_size)
   
@login_required(login_url='/accounts/login/')
def set_persistentnats(request,num):
    return set_list(request,to_set=models.Userpnat,sender=models.Persistentnat,reciever='events',num=num,list_size=persistentnat_list_size)

@login_required(login_url='/accounts/login/')
def set_events(request,num):
    return set_list(request,to_set=models.Userevent,sender=models.Eventlist,reciever='events',num=num,list_size=event_list_size)

@login_required(login_url='/accounts/login/')
def show_depressionquiz(request):
    #return HttpResponse(depression_list)
    if not request.user.is_authenticated():
        return render(request,'cbt2/base.html')    
    return render(request,'cbt2/depression.html',{'quiz_list': depression_list})

def show_anxietyquiz(request):
    return render(request,'cbt2/anxiety.html',{'quiz_list': anxiety_list})
