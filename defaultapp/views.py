

from django.http import HttpResponseRedirect,HttpResponse, HttpRequest
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render,render_to_response ,redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.core.urlresolvers import reverse
from django.core import serializers
from django.shortcuts import  get_object_or_404 , get_list_or_404
from django.views.decorators.cache import cache_control
from django.utils.crypto import get_random_string
from datetime import datetime
from .models import * 
from django.contrib.auth.decorators import login_required
from django.conf import settings
from cbt2.models import *
from exercise.models import *
from conversationmanager.models import *

from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
#----------------------------------------------------------------------
def modulemanager(request):
    try:
        module_number=request.session['module_number']
    except (KeyError):
        return HttpResponseRedirect("/welcome/")
    else:
        
        technique_list=Technique.objects.filter(module_number=module_number).order_by('technique_id')
        exercise_list=ConversationToModule.objects.filter(module_number=module_number).values('conversationID').distinct()
        data={'technique_list':technique_list,'module_number':module_number,'exercise_list':exercise_list }
        return render(request,'defaultapp/module_main_page.html',data)
@login_required(login_url='/accounts/login/')
#----------------------------------------------------------------------
def moduletechnique(request):
    if request.POST.get('module_number') == None:
        try:
            module_number=request.session['module_number']
            user=request.user
                #return HttpResponse(user)
            technique=get_object_or_404(Technique,technique_id=int(request.session['technique']))
            defaultconversations=DefaultConversation.objects.filter(technique=technique)
            defaultconversationset=defaultconversations.values_list('conversationID',flat=True)
            specificonversations=UserConversationTechnique.objects.filter(user=user,technique=technique).values_list('conversation',flat=True)
            #return HttpResponse(specificonversations)
            defaulthistories=ConversationHistory.objects.filter(user=user,conversationID__in=defaultconversationset)
            specifichistories=ConversationHistory.objects.filter(user=user,conversationID__in=specificonversations)
            #return HttpResponse(history)
            data={'user':request.user.get_username(),
                  'defaultconversations' : defaultconversations,
                  'specificonversations' : specificonversations,
                  'defaulthistories'     : defaulthistories,
                  'specifichistories'    : specifichistories,
                  }
            return render(request,'defaultapp/conversation_page.html',data)            
            
        except KeyError:
            return HttpResponseRedirect('/welcome/')
        #module_number=request.POST.get('module_number')
        
@login_required(login_url='/accounts/login/')
#----------------------------------------------------------------------
def show_list(request):
        technique=get_object_or_404(Technique,technique_id=int(request.POST.get('technique')))
        request.session['technique']=request.POST.get('technique')
        user=request.user
        is_list_shown,created=ShownListToUser.objects.get_or_create(user=user,technique=technique)
        if is_list_shown.status :
            return HttpResponseRedirect('/technique/')
        list_to_show=ShowTechniqueBeliefsEventsNats.objects.filter(technique=technique)
        return render(request,'defaultapp/show_list.html',{'list_to_show':list_to_show ,'technique':technique})

@login_required(login_url='/accounts/login/')
#----------------------------------------------------------------------
def set_list(request):
    technique=get_object_or_404(Technique,technique_id=int(request.POST.get('technique')))
    user=request.user
    for i in range (0,int(request.POST.get('list_length'))):
        if not request.POST.get('elements%d' %(i+1),None) == None:
            beliefseventsnats=get_object_or_404(BeliefsEventsNats,beliefseventsnatsID=int(request.POST.get('elements%d' %(i+1))))
            done=UserBeliefsEventsNats.objects.get_or_create(user=user,beliefs_events_nats=beliefseventsnats)
            found_conversations=ConversationTechniqueBeliefsEventsNats.objects.filter(technique=technique,beliefseventsnats=beliefseventsnats)
            for conversations in found_conversations:
                add_conversation=UserConversationTechnique.objects.get_or_create(user=user,technique=technique,conversation=conversations.conversation)
    is_list_shown=get_object_or_404(ShownListToUser,user=user,technique=technique)
    is_list_shown.status=True
    is_list_shown.save()
    response=HttpResponse(is_list_shown.status)
    
    return response
    