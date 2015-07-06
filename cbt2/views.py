###########################################
# importing neccessary class and modules 
###########################################
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
"""
depression assessment quiz question list
NOT USED ANYWHERE YET
"""
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
"""
anxiety assessment quiz question list
NOT USED ANYWHERE YET
"""
"""
NOTE:- EVERY VIEW WITH @login_required(login_url='/accounts/login/') DECORATOR WILL ONLY BE ACCESSED IF ONLY AFTER A USER LOGIN
"""
anxiety_list=[
    'Feeling nervous, anxious or on edge',
    'Not being able to stop or control worrying',
    'Worrying too much about different things',
    'Trouble relaxing',
    'Being so restless that it is hard to sit still',
    'Becoming easily annoyed or irritable',
    'Feeling afraid as if something awful might happen',
]
#function to generate random string [NOT USED YET]
def random_uid():
    unique_id=get_random_string(length=25)
    return unique_id


# renders request to home page
#----------------------------------------------------------------------
def home(request):
    return render(request,'cbt2/home.html')

"""
this is a view to render welcome page. the page will only be rendered if the user completes his profile first.
"""
#----------------------------------------------------------------------
@login_required(login_url='/accounts/login/')
def welcome(request):
    userdetail=models.Customuserprofile.objects.filter(user=request.user)
    if userdetail.exists():
        return render(request,'cbt2/welcome.html')
    else:
        return HttpResponseRedirect('/fill/details/')
#----------------------------------------------------------------------
"""
this is view that is used for user sign up purpose it uses signupform ('cbt2/forms.py').
initailly we check if the method in request is POST or not if it is POST we pass the post data in our signupform (function call forms.signupform(request.POST))
if method is GET we simply return  the empty form
for post method we check if form is valid and if it is we save the form to create user
after the user is created we create a test boject for the user to keep his depression and anxiety score
"""
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
            return HttpResponseRedirect('/accounts/login/')
    return render(request,'cbt2/usersignup.html',{'form':form})

#----------------------------------------------------------------------
"""
this view simply render the login page
"""
def login(request):
    c = {}
    c.update(csrf(request))
    return render(request,'cbt2/login.html') 
#----------------------------------------------------------------------
"""
this view read the post method data: username and password and call the auth.authenticate(username=username, password=password)
this function call return an object of setting.AUTH_USER_MODEL if the given credential are correct for registered user
then if the user is a superuser, user is directed to admin_page by returning HttpResponseRedirect('/admin_page/')
and a regualr user is directed to '/welcom/' page by returning HttpResponseRedirect('/welcome/')
if the credential are false the user is shown invalid user page

"""
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

#----------------------------------------------------------------------
"""
this is a view to redirect the user to once he is logged in
"""
def loggedin(request):
    if(request.GET['next']==None):
        return HttpResponseRedirect('/home/')
    else:
        return HttpResponseRedirect(request.GET['next'])
    
#----------------------------------------------------------------------
"""
if the credentials are incorrect then the user is rendered a page showing incorrect credentials 
"""
def invalid_login(request):
    return render(request,'cbt2/invalid_login.html')

#----------------------------------------------------------------------
"""
this view logs out the user also delete the cache history so that user can't log back in just by pressing back button in browser
"""
@cache_control(no_cache=True, must_revalidate=True)
# function that log out user
def logout(request):
    auth.logout(request)
    response=redirect('cbt2.views.login')
    
    return response


#----------------------------------------------------------------------
"""
this function uses userdetails form and pass the filled fields if the request is post otherwise renders the same form
also if the form is valid it create (not exists already and if exists it will update it ) a user profile for the user 
"""
@login_required(login_url='/accounts/login')
def user_details(request):
    if request.method == 'GET':
        form=userdetails()
    else:
        form=userdetails(request.POST)
        if form.is_valid():
            user=request.user
            age=form.cleaned_data['agegroup']
            edu=form.cleaned_data['education']
            country=form.cleaned_data['country']
            occu=form.cleaned_data['enrolled_as']
            gen=form.cleaned_data['gender']
            phno=form.cleaned_data['ph']
            done=models.Customuserprofile.objects.filter(user=user)
            if done.exists():
                done.update(agegroup=age,education=edu,country=country,enrolled_as =occu,gender=gen,phonenumber=phno)
            else:
                models.Customuserprofile.objects.create(user=user,agegroup=age,education=edu,country=country,enrolled_as =occu,gender=gen,phonenumber=phno)
            args ={}
            args.update(csrf(request))
            return HttpResponseRedirect('/fill/family_details/')
    return render(request,'cbt2/userinfo.html',{'form': form})
    


#----------------------------------------------------------------------
"""
this view uses familydetails form and pass the filled fields if the request is post otherwise renders the same form
also if the form is valid it create if(not exists already and if exists it will update it ) a user's family member profile for the user by exeuting create query
"""
@login_required(login_url='/accounts/login/')
def family_details(request):
    if request.method == 'GET':
        form=familydetails()
    else:
        form=familydetails(request.POST)
        if form.is_valid():
            user=request.user
            #request.session['userid']=user
            mname=form.cleaned_data['member_name']
            eid=form.cleaned_data['emailid']
            phno=form.cleaned_data['ph']
            rtou=form.cleaned_data['relate']
            #invoid=form.cleaned_data['involvementid']
            done=models.Familymembers.objects.filter(user=user)
            if done.exists():
                done.update(member_name=mname,emailid=eid,phonenumber=phno,relate=rtou)
            else:
                models.Familymembers.objects.create(user=user,member_name=mname,emailid=eid,phonenumber=phno,relate=rtou)
            args = {}
            args.update(csrf(request))
            return HttpResponseRedirect("/user/setting/")
    return render(request,'cbt2/userfamilyinfo.html',{'form': form})

#----------------------------------------------------------------------
"""
this view renders a form for taking user's familymember's involvement 
if user tries to fill this before registering a member he/she will be directed to first fill the family member detail
"""
@login_required(login_url='/accounts/login/')
def settings(request):
    if request.method == 'GET':
        form=involvement()
    else:
        form=involvement(request.POST)
        if form.is_valid():
            user=request.user
            invo=form.cleaned_data['involvement']
            try :
                models.Familymembers.objects.get(user=user).update(involvementid=invo)
            except models.Familymembers.DoesNotExist:
                return HttpResponseRedirect('/fill/family_details/')
            return HttpResponseRedirect('/depression_quiz/')
    return render(request,'cbt2/setting.html',{'form':form})

#----------------------------------------------------------------------
"""
this view is used for setting depression assessment score of the user as per module/week.
if the depression score is already set for the module he/she will be directed to anxiety assessment quiz
"""
@login_required(login_url='/accounts/login/')
def set_depression_score(request):
    user=request.user
    module_number=request.POST.get('module_number')
    score=request.POST.get('score')
    user_test=models.Test.objects.get(user=user)
    if module_number == '1':
        user_test.dsasweek1=score
    elif module_number == '2':
        user_test.dsasweek2=score
    elif module_number == '3':
        user_test.dsasweek3=score
    elif module_number == '4':
        user_test.dsasweek4=score
    elif module_number == '5':
        user_test.dsasweek5=score
    elif module_number == '6':
        user_test.dsasweek6=score
    elif module_number == '7':
        user_test.dsasweek7=score
    user_test.save()
    return HttpResponseRedirect("/anxiety_quiz/")

#----------------------------------------------------------------------
"""
this view is used for setting anxiety assessment score of the user as per module/week.
if the anxiety score is already set for the module he/she will be directed to module main page
"""
@login_required(login_url='/accounts/login/')
def set_anxiety_score(request):
    user=request.user
    module_number=request.POST.get('module_number')
    score=request.POST.get('score')
    user_test=models.Test.objects.get(user=user)
    if module_number == '1':
        user_test.asweek1=score
    elif module_number == '2':
        user_test.asweek2=score
    elif module_number == '3':
        user_test.asweek3=score
    elif module_number == '4':
        user_test.asweek4=score
    elif module_number == '5':
        user_test.asweek5=score
    elif module_number == '6':
        user_test.asweek6=score
    elif module_number == '7':
        user_test.asweek7=score
    user_test.save()
    #return HttpResponseRedirect("/module/")
    if module_number == '1':
        return HttpResponseRedirect('/Psychoeducation about Depression and CBT/')
    elif module_number == '2':
        return HttpResponseRedirect('/Behavioral Activation/')
    elif module_number == '3':
        return HttpResponseRedirect('/Identifying NATs/')
    elif module_number == '4':
        return HttpResponseRedirect('/Challenging NATs/')
    elif module_number == '5':
        return HttpResponseRedirect('/Modifying Intermediate and Core Beliefs/')
    elif module_number == '6':
        return HttpResponseRedirect('/Relapse Prevention/')
    else:
        return HttpResponseRedirect('/welcome/')    
        
    
#----------------------------------------------------------------------
"""
this view is used for showing depression assessment score of the user as per module/week.
"""
@login_required(login_url='/accounts/login/')
def show_depressionquiz(request):
    module_number=request.POST.get('module_number',None)
    user=request.user
    #return HttpResponse(module_number)
    if module_number == None:
        return HttpResponseRedirect('/welcome/')
    request.session['module_number']=module_number
    user_test=models.Test.objects.get(user=user)
    #return HttpResponse(not user_test.dsasweek1 )
    if module_number == '1':
        if not user_test.dsasweek1 :
            return render(request,'cbt2/depression_assessment_questionnaire.html',{'module_number':module_number})
    elif module_number == '2':
        if not user_test.dsasweek2 :
            return render(request,'cbt2/depression_assessment_questionnaire.html',{'module_number':module_number})
    elif module_number == '3':
        if not user_test.dsasweek3 :
            return render(request,'cbt2/depression_assessment_questionnaire.html',{'module_number':module_number})
    elif module_number == '4':
        if not user_test.dsasweek4 :
            return render(request,'cbt2/depression_assessment_questionnaire.html',{'module_number':module_number})
    elif module_number == '5':
        if not user_test.dsasweek5:
            return render(request,'cbt2/depression_assessment_questionnaire.html',{'module_number':module_number})
    elif module_number == '6':
        if not user_test.dsasweek6 :
            return render(request,'cbt2/depression_assessment_questionnaire.html',{'module_number':module_number})
    else:
        return render(request,'cbt2/depression_assessment_questionnaire.html',{'module_number':module_number})
    return HttpResponseRedirect('/anxiety_quiz/')

#----------------------------------------------------------------------
"""
this view is used for showing anxiety assessment score of the user as per module/week.
"""
@login_required(login_url='/accounts/login/')
def show_anxietyquiz(request):
    module_number=request.session['module_number']
    user=request.user
    user_test=models.Test.objects.get(user=user)
    if module_number == '1':
        if not user_test.asweek1:
            return render(request,'cbt2/anxiety_assesment_questionnaire.html',{'module_number':module_number})
    elif module_number == '2':
        if not user_test.asweek2 :
            return render(request,'cbt2/anxiety_assesment_questionnaire.html',{'module_number':module_number})
    elif module_number == '3':
        if not user_test.asweek3:
            return render(request,'cbt2/anxiety_assesment_questionnaire.html',{'module_number':module_number})
    elif module_number == '4':
        if not user_test.asweek4 :
            return render(request,'cbt2/anxiety_assesment_questionnaire.html',{'module_number':module_number})
    elif module_number == '5':
        if not user_test.asweek5 :
            return render(request,'cbt2/anxiety_assesment_questionnaire.html',{'module_number':module_number})
    elif module_number == '6':
        if not user_test.asweek6 :
            return render(request,'cbt2/anxiety_assesment_questionnaire.html',{'module_number':module_number})
    elif module_number == '7':
        return render(request,'cbt2/anxiety_assesment_questionnaire.html',{'module_number':module_number})
    if module_number == '1':
        return HttpResponseRedirect('/Psychoeducation about Depression and CBT/')
    elif module_number == '2':
        return HttpResponseRedirect('/Behavioral Activation/')
    elif module_number == '3':
        return HttpResponseRedirect('/Identifying NATs/')
    elif module_number == '4':
        return HttpResponseRedirect('/Challenging NATs/')
    elif module_number == '5':
        return HttpResponseRedirect('/Modifying Intermediate and Core Beliefs/')
    elif module_number == '6':
        return HttpResponseRedirect('/Relapse Prevention/')
    else:
        return HttpResponseRedirect('/welcome/')
    
       
   
