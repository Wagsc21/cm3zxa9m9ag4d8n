from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render,render_to_response ,redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.core.urlresolvers import reverse
from django.core import serializers
from django.views.decorators.cache import cache_control
from django.utils.crypto import get_random_string
from datetime import datetime
from . import models 
from django.contrib.auth.decorators import login_required
from django.conf import settings

   
#----------------------------------------------------------------------
def modulemanager(request):
    module_number=request.session['module_number']
    if module_number == None:
        return HttpResponseRedirect("/welcome/")
    else:
        
        technique_list=models.DefaultConversation.objects.filter(module_number=module_number).values('technique').distinct()
        exercise_list=models.ConversationToModule.objects.filter(module_number=module_number)
        data={'technique_list':technique_list,'module_number':module_number,'exercise_list':exercise_list }
        return render(request,'defaultapp/module_main_page.html',data)

#----------------------------------------------------------------------
def moduletechnique(request):
    if request.POST.get('module_number') == None:
        return HttpResponseRedirect("/welcome/")
    else:
        module_number=request.POST.get('module_number')
        technique=request.POST.get('technique')
        user=request.user
        #return HttpResponse(user)
        
        conversations=models.DefaultConversation.objects.filter(module_number=module_number,technique=technique)
        CID=conversations.values("conversationID")
        ibset=models.Usersib.objects.filter(user=user).values('intermediatebelief')
        cbset=models.Userscb.objects.filter(user=user).values('corebelief')
        pnatset=models.Userpnat.objects.filter(user=user).values('persistentnat')
        eventset=models.Userevent.objects.filter(user=user).values('event')        
        ibconversations=models.IntermediatebeliefConversation.objects.filter(module_number=module_number,technique=technique,intermediatebelief__in=ibset)
        cbconversations=models.CorebeliefConversation.objects.filter(module_number=module_number,technique=technique,corebelief__in=cbset)
        pnatconversations=models.PersistentnatConversation.objects.filter(module_number=module_number,technique=technique,persistentnat__in=pnatset)
        eventlistconversations=models.EventlistConversation.objects.filter(module_number=module_number,technique=technique,eventlist__in=eventset)
        history_conversations=models.ConversationHistory.objects.filter(user=user,conversationID__in=CID)
        CBID=cbconversations.values("conversationID")
        IBID=ibconversations.values("conversationID")
        PNATID=pnatconversations.values("conversationID")
        EID=eventlistconversations.values("conversationID")
        history_cbconversations=models.ConversationHistory.objects.filter(user=user,conversationID__in=CBID)
        history_ibconversations=models.ConversationHistory.objects.filter(user=user,conversationID__in=IBID)
        history_pnatconversations=models.ConversationHistory.objects.filter(user=user,conversationID__in=PNATID)
        history_eventlistconversations=models.ConversationHistory.objects.filter(user=user,conversationID__in=EID)
        #return HttpResponse(ibconversations)
        #conversations=list(set(conversations))
        data={'user':request.user.get_username(),
              'conversations': conversations,
              'ibconversations': ibconversations,
              'pnatconversations': pnatconversations,
              'history_conversations': history_conversations,
              'eventlistconversations': eventlistconversations,
              "history_ibconversations": history_ibconversations,
              'history_cbconversations': history_cbconversations,
              'history_pnatconversations': history_pnatconversations,
              'history_eventlistconversations': history_eventlistconversations,
              }
        return render(request,'defaultapp/conversation_page.html',data)
    