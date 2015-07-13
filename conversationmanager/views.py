######################################################
# all neccessary modules and classes are imported
#######################################################
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render,render_to_response , get_object_or_404 , get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect 
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
#from .forms import * 
from django.core import serializers
from django.views.decorators.cache import cache_control
from django.utils.crypto import get_random_string
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q , Max
"""
this view is used to carry out the conversation (or simply traversing the Conversationoptiongraph model )
this view reads a dialog form the post method if it is none den it assumes it is a start of the conversation.
in that case it look for a conversationID in the post data of the request
if the conversationID is found is fatches the first dialog for it and from the Conversationoptiongraph it fatches options for that dialog.
after that it renders the data to the conversation page.
that page makes ajax request and from that on this view read the dialog and selected option and find out the next_dialog
once next dialog is found it again fatches options for that and render to the same page untill the no option is found for the dialog
"""
@login_required(login_url='/accounts/login/')
def carry_out_conversation(request):
    user=request.user
        
    if not request.POST.get('dialog',None) == None:
        
        if not request.POST.get('option',None) == None:
            try :
                dialog=models.Dialogs.objects.get(dialog=int(request.POST['dialog']))
                #return HttpResponse(request.POST['dialog'])
                conversationID=models.Conversation.objects.get(conversationID=int(request.session['conversationID']))
                option=models.Options.objects.get(optionID= int(request.POST['option']))
                qset=models.Conversationoptiongraph.objects.filter(current_dialog = dialog, option =option)
                optionset=models.Conversationoptiongraph.objects.filter(current_dialog=qset[0].next_dialog)
                dialog=qset[0].next_dialog
                option_list=[]
                for opt in optionset:
                    option_list.append(opt.option)
                #models.Userconversation.objects.create(user=user,dialog=qset[0].current_dialog,option_selected=qset[0].option,conversation_time=datetime.now(),conversationID=conversationID)
                return render(request,'conversationmanager/conversation.html',{'option_list': option_list,'dialog':dialog,'conversationID':request.session['conversationID']})
            except(KeyError):
                return HttpResponse('keyerror in carrying it out')
    
    else:
        try:
            conversationID=models.Conversation.objects.get(conversationID=request.POST['conversationID'])
            fullconversationset=models.Dialogs.objects.filter(conversationID=conversationID).order_by('dialog')
            optionset=models.Conversationoptiongraph.objects.filter(current_dialog = fullconversationset[0])
            request.session['conversationID']=request.POST['conversationID']
            option_list=[]
            for opt in optionset:
                option_list.append(opt.option)
            #models.Userconversation.objects.create(user=user,conversation=fullconversationset[0],option_selected=qset[0].option,conversation_time=datetime.now())
            return render(request,'conversationmanager/conversation.html',{'option_list': option_list,'dialog':fullconversationset[0],'conversationID':request.session['conversationID']})
        except(KeyError):
            return HttpResponseRedirect('/welcome/')

    
"""
this page has to be used only by admin it is used for adding new conversation this renders a page which shows.
it renders a page to add dialogs and options for the conversation
"""

#----------------------------------------------------------------------
@user_passes_test(lambda u: u.is_superuser)
def conversation(request):
    last_conversation=models.Conversation.objects.all().aggregate(Max('conversationID'))['conversationID__max']
    return render(request,"conversationmanager/myui.html",{'lastconversation': last_conversation})

"""
this view handles the addition of new conversations.
it first create object of the dialogs
then for every option it search for an existing one and if one exists it uses that otherwise it creates one.
then it creates the graph for the dialog and options (current_dialog<-->option<-->next_dialog)
"""

#----------------------------------------------------------------------
@user_passes_test(lambda u: u.is_superuser)
def add_conversation(request):
    if request.POST.get('conversationid') ==None:
        return HttpResponseRedirect("/admin_page/")
    conversation=models.Conversation.objects.filter(conversationID=int(request.POST.get('conversationid')))
    if conversation.exists():
        return render(request,"conversationmanager/goback.html",{'message':'%s already exist' % request.POST.get('conversationid')})    
    conversationID=models.Conversation.objects.create(conversationID=int(request.POST.get('conversationid')))
    i=0
    while (not request.POST.get('row[%d][0]' %i, None) == None):
        last_dialog_ID=models.Dialogs.objects.all().aggregate(Max('dialog'))['dialog__max']
        last_option_ID=models.Options.objects.all().aggregate(Max('optionID'))['optionID__max']
        #i=i+1
        
            

        try:
            current_dialog=models.Dialogs.objects.get(Q(conversationID=conversationID),Q(dialog_text=request.POST.get('row[%d][0]' %i)))
        except:
            current_dialog=models.Dialogs.objects.create(dialog=last_dialog_ID+1,conversationID=conversationID,dialog_text=request.POST.get('row[%d][0]' %i))
            last_dialog_ID=models.Dialogs.objects.latest("dialog").dialog
        try:
            next_dialog=models.Dialogs.objects.get(Q(conversationID=conversationID),Q(dialog_text=request.POST.get('row[%d][2]' %i)))
        except:
            next_dialog=models.Dialogs.objects.create(conversationID=conversationID,dialog=last_dialog_ID+1,dialog_text=request.POST.get('row[%d][2]' %i))
            last_dialog_ID=models.Dialogs.objects.latest("dialog").dialog
        try:
            option=models.Options.objects.get(Q(option_text=request.POST.get('row[%d][1]' %i)))
        except models.Options.DoesNotExist:
            option=models.Options.objects.create(optionID=last_option_ID+1 ,option_text=request.POST.get('row[%d][1]' %i))
        wrong_option=False
        if not request.POST.get('is_correct[%d]'%i,None) == None:
            wrong_option=True
        models.Conversationoptiongraph.objects.get_or_create(current_dialog=current_dialog,option=option,next_dialog=next_dialog,wrogn_option=wrong_option)
        i=i+1
    return render(request,"conversationmanager/goback.html",{'message':'%s added' % request.POST.get('conversationid')})

"""
this view renders the admin page
"""

#----------------------------------------------------------------------
@user_passes_test(lambda u: u.is_superuser)
def admin(request):
    return render(request,'conversationmanager/admin_page.html')

"""
this view renders the update page 
"""
#----------------------------------------------------------------------
@user_passes_test(lambda u: u.is_superuser)

def update_conversation(request):
    return render(request,'conversationmanager/editui.html')

"""
this view render the row of an existing conversationID send in post request in case
if the given conversationID doesn't exist it shows a error message and it the conversationID exist in the database
it returns all the rows of the conversationID as a graph (current_dialog<-->option<-->next_dialog)
"""

#----------------------------------------------------------------------
@user_passes_test(lambda u: u.is_superuser)
def edit_conversation(request):
    conversation=models.Conversation.objects.filter(Q(conversationID=int(request.POST.get('conversationid'))))
    if not conversation.exists():
        return render(request,"conversationmanager/errorinedit.html",{'message':'%s does not exist' % request.POST.get('conversationid')})
    dialogs=models.Dialogs.objects.filter(conversationID__in=conversation)
    rows=models.Conversationoptiongraph.objects.filter(current_dialog__in=dialogs).order_by("current_dialog")
    return render(request,'conversationmanager/editpage.html',{'rows':rows,'conversationid':request.POST.get('conversationid')})
   

"""
this view apply the updates of edit done in the conversation
for applying update it first delete all the previous dialogs and new ones
"""

#----------------------------------------------------------------------
@user_passes_test(lambda u: u.is_superuser)
def apply_update(request):
    i=1
    conversationid=models.Conversation.objects.get(conversationID=int(request.POST.get('conversationid')))
    conversations=models.Dialogs.objects.filter(conversationID=conversationid).delete()
    i=1
    while (not request.POST.get('row[%d][0]' %i, None) == None):
        last_dialog_ID=models.Dialogs.objects.all().aggregate(Max('dialog'))['dialog__max']
        if last_dialog_ID==None:
            last_dialog_ID=0
        last_option_ID=models.Options.objects.all().aggregate(Max('optionID'))['optionID__max']
        if last_option_ID == None:
            last_option_ID=0
        try:
            current_dialog=models.Dialogs.objects.get(Q(conversationID=conversationid),Q(dialog_text=request.POST.get('row[%d][0]' %i)))
        except:
            current_dialog=models.Dialogs.objects.create(dialog=last_dialog_ID+1,conversationID=conversationid,dialog_text=request.POST.get('row[%d][0]' %i))
            last_dialog_ID=models.Dialogs.objects.latest("dialog").dialog
        try:
            next_dialog=models.Dialogs.objects.get(Q(conversationID=conversationid),Q(dialog_text=request.POST.get('row[%d][2]' %i)))
        except:
            next_dialog=models.Dialogs.objects.create(conversationID=conversationid,dialog=last_dialog_ID+1,dialog_text=request.POST.get('row[%d][2]' %i))
            last_dialog_ID=models.Dialogs.objects.latest("dialog").dialog
        try:
            option=models.Options.objects.get(Q(option_text=request.POST.get('row[%d][1]' %i)))
        except models.Options.DoesNotExist:
            option=models.Options.objects.create(optionID=last_option_ID+1 ,option_text=request.POST.get('row[%d][1]' %i))
        wrong_option=False
        if not request.POST.get('is_correct[%d]'%i,None) == None:
            wrong_option=True        
        models.Conversationoptiongraph.objects.get_or_create(current_dialog=current_dialog,option=option,next_dialog=next_dialog,wrong_option=wrong_option)
        i=i+1
    #conversations=models.Dialogs.objects.filter(conversationID=conversationid).delete()
    
    return edit_conversation(request)

"""
this view  at the end of a conversation it saves the history string for the user
"""
#----------------------------------------------------------------------
@login_required(login_url='/accounts/login/')
def history(request):
    user=request.user
    conversationID=models.Conversation.objects.get(conversationID=int(request.POST.get('conversationID')))
    #HttpResponse(request.POST.get('conversationID'))
    try:
        history=models.ConversationHistory.objects.get(user=user,conversationID=conversationID)
        history.history=request.POST.get('history')
        history.save()
        #return HttpResponse(request.POST.get('history'))
        return render(request,{'history':request.POST.get('history')})
    except models.ConversationHistory.DoesNotExist:
        history=models.ConversationHistory.objects.create(user=user,conversationID=conversationID,history=request.POST.get('history'))
        return HttpResponse('history created')

"""
this view is used for showing the list of the conversations which are carried out atlest one and are in user's history.
also when a conversationID is selected it shows the user history for the conversation
"""  
#----------------------------------------------------------------------
@login_required(login_url='/accounts/login/')
def show_history(request):
    user=request.user
    if request.POST.get('conversationID',None) == None:
        return HttpResponseRedirect("/welcome/")
    conversation=get_object_or_404(models.Conversation,conversationID=int(request.POST.get('conversationID')))    
    try:
        history=models.ConversationHistory.objects.get(user=user,conversationID=conversation)
        return render(request,'conversationmanager/show_history.html',{'history': history,'conversationID':request.POST.get('conversationID')})
    except models.ConversationHistory.DoesNotExist:
        return HttpResponse("NO history")
    #return HttpResponse('error')
   
