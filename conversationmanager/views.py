from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render,render_to_response , get_object_or_404 , get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect 
from django.core.urlresolvers import reverse
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
# Create your views here.
#"""
 
 # function for carrying out the conversation with conversation id as only input
def carry_out_conversation(request):
    """
    try:
        username=request.session['username']
        user=User.objects.get(username=username)
    except:
        return HttpResponseRedirect('/accounts/login/')
    """
    username=request.session['username']
    user=User.objects.get(username=username)    
    if not request.POST.get('dialog',None) == None:
        
        if not request.POST.get('option',None) == None:
            try :
                dialog=models.Conversations.objects.get(dialog=int(request.POST['dialog']))
                #return HttpResponse(request.POST['dialog'])
                option=models.Options.objects.get(optionID= int(request.POST['option']))
                qset=models.Conversationoption.objects.filter(current_conversation = dialog, option =option)
                optionset=models.Conversationoption.objects.filter(current_conversation=qset[0].next_conversation)
                dialog=qset[0].next_conversation
                option_list=[]
                for opt in optionset:
                    option_list.append(opt.option)
                models.Userconversation.objects.create(user=user,conversation=qset[0].current_conversation,option_selected=qset[0].option,conversation_time=datetime.now(),conversationID=request.session['conversationID'])
                return render(request,'conversationmanager/conversation.html',{'option_list': option_list,'dialog':dialog})
            except(KeyError):
                return HttpResponse('keyerror in carrying it out')
    
    else:
        try:
            fullconversationset=models.Conversations.objects.filter(conversationID=request.POST['conversation']).order_by('dialog')
            optionset=models.Conversationoption.objects.filter(current_conversation= fullconversationset[0])
            request.session['conversationID']=request.POST['conversation']
            option_list=[]
            for opt in optionset:
                option_list.append(opt.option)
            #models.Userconversation.objects.create(user=user,conversation=fullconversationset[0],option_selected=qset[0].option,conversation_time=datetime.now())
            return render(request,'conversationmanager/conversation.html',{'option_list': option_list,'dialog':fullconversationset[0]})
        except(KeyError):
            return HttpResponse('keyerror in start')
#"""   
    
def conversation_page(request):
    conversations=models.Conversations.objects.values_list("conversationID",flat=True).distinct()
    conversations=list(set(conversations))
    return render(request,'conversationmanager/conversation_page.html',{'conversations': conversations})


@user_passes_test(lambda u: u.is_superuser)
#----------------------------------------------------------------------
def conversation(request):
    last_conversation=models.Conversations.objects.all().aggregate(Max('conversationID'))['conversationID__max']
    return render(request,"conversationmanager/myui.html",{'lastconversation': last_conversation})

@user_passes_test(lambda u: u.is_superuser)
#----------------------------------------------------------------------
def add_conversation(request):
    conversation=models.Conversations.objects.filter(Q(conversationID=int(request.POST.get('conversationid'))))
    conversation=list(conversation)
    if not len(conversation) == 0:
        return render(request,"conversationmanager/goback.html",{'message':'%s already exist' % request.POST.get('conversationid')})    
    
    i=0
    while (not request.POST.get('row[%d][0]' %i, None) == None):
        last_dialog_ID=models.Conversations.objects.all().aggregate(Max('dialog'))['dialog__max']
        last_option_ID=models.Options.objects.all().aggregate(Max('optionID'))['optionID__max']
        #i=i+1
        
            

        try:
            current_dialog=models.Conversations.objects.get(Q(conversationID=int(request.POST.get('conversationid'))),Q(dialog_text=request.POST.get('row[%d][0]' %i)))
        except:
            current_dialog=models.Conversations.objects.create(dialog=last_dialog_ID+1,conversationID=int(request.POST.get('conversationid')),dialog_text=request.POST.get('row[%d][0]' %i))
            last_dialog_ID=models.Conversations.objects.latest("dialog").dialog
        try:
            next_dialog=models.Conversations.objects.get(Q(conversationID=int(request.POST.get('conversationid'))),Q(dialog_text=request.POST.get('row[%d][2]' %i)))
        except:
            next_dialog=models.Conversations.objects.create(conversationID=int(request.POST.get('conversationid')),dialog=last_dialog_ID+1,dialog_text=request.POST.get('row[%d][2]' %i))
            last_dialog_ID=models.Conversations.objects.latest("dialog").dialog
        try:
            option=models.Options.objects.get(Q(option_text=request.POST.get('row[%d][1]' %i)))
        except models.Options.DoesNotExist:
            option=models.Options.objects.create(optionID=last_option_ID+1 ,option_text=request.POST.get('row[%d][1]' %i))
        models.Conversationoption.objects.get_or_create(current_conversation=current_dialog,option=option,next_conversation=next_dialog)
        i=i+1
    return render(request,"conversationmanager/goback.html",{'message':'%s added' % request.POST.get('conversationid')})

@user_passes_test(lambda u: u.is_superuser)
#----------------------------------------------------------------------
def admin(request):
    return render(request,'conversationmanager/admin_page.html')

@user_passes_test(lambda u: u.is_superuser)
#----------------------------------------------------------------------
def update_conversation(request):
    return render(request,'conversationmanager/editui.html')
@user_passes_test(lambda u: u.is_superuser)
#----------------------------------------------------------------------
def edit_conversation(request):
    conversation=models.Conversations.objects.filter(Q(conversationID=int(request.POST.get('conversationid'))))
    x=list(conversation)
    if len(x) == 0:
        return render(request,"conversationmanager/errorinedit.html",{'message':'%s does not exist' % request.POST.get('conversationid')})
    rows=models.Conversationoption.objects.filter(current_conversation__in=conversation).order_by("current_conversation")
    return render(request,'conversationmanager/editpage.html',{'rows':rows,'conversationid':request.POST.get('conversationid')})
   
@user_passes_test(lambda u: u.is_superuser)
#----------------------------------------------------------------------
def apply_update(request):
    i=1
    conversationid=int(request.POST.get('conversationid'))
    conversations=models.Conversations.objects.filter(conversationID=conversationid).delete()
    i=1
    while (not request.POST.get('row[%d][0]' %i, None) == None):
        last_dialog_ID=models.Conversations.objects.all().aggregate(Max('dialog'))['dialog__max']
        last_option_ID=models.Options.objects.all().aggregate(Max('optionID'))['optionID__max']
        try:
            current_dialog=models.Conversations.objects.get(Q(conversationID=int(request.POST.get('conversationid'))),Q(dialog_text=request.POST.get('row[%d][0]' %i)))
        except:
            current_dialog=models.Conversations.objects.create(dialog=last_dialog_ID+1,conversationID=int(request.POST.get('conversationid')),dialog_text=request.POST.get('row[%d][0]' %i))
            last_dialog_ID=models.Conversations.objects.latest("dialog").dialog
        try:
            next_dialog=models.Conversations.objects.get(Q(conversationID=int(request.POST.get('conversationid'))),Q(dialog_text=request.POST.get('row[%d][2]' %i)))
        except:
            next_dialog=models.Conversations.objects.create(conversationID=int(request.POST.get('conversationid')),dialog=last_dialog_ID+1,dialog_text=request.POST.get('row[%d][2]' %i))
            last_dialog_ID=models.Conversations.objects.latest("dialog").dialog
        try:
            option=models.Options.objects.get(Q(option_text=request.POST.get('row[%d][1]' %i)))
        except models.Options.DoesNotExist:
            option=models.Options.objects.create(optionID=last_option_ID+1 ,option_text=request.POST.get('row[%d][1]' %i))
        models.Conversationoption.objects.get_or_create(current_conversation=current_dialog,option=option,next_conversation=next_dialog)
        i=i+1
    return edit_conversation(request)
   
