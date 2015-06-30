from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render,render_to_response ,redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.core.urlresolvers import reverse
#from .forms import * 
from django.core import serializers
from django.views.decorators.cache import cache_control
from django.utils.crypto import get_random_string
from datetime import datetime
from . import models 
from django.contrib.auth.decorators import login_required
from django.conf import settings

   
#----------------------------------------------------------------------
def modulemanager(request):
    if request.POST.get('module_number') == None:
        return HttpResponseRedirect("/welcome/")
    else:
        module_number=request.POST.get('module_number')
        technique_list=models.DefaultConversation.objects.filter(module_number=module_number).values('technique').distinct()
        return render(request,'defaultapp/module_main_page.html',{'technique_list':technique_list,'module_number':module_number})

#----------------------------------------------------------------------
def moduletechnique(request):
    if request.POST.get('module_number') == None:
        return HttpResponseRedirect("/welcome/")
    else:
        module_number=request.POST.get('module_number')
        technique=request.POST.get('technique')
        conversations=models.DefaultConversation.objects.filter(module_number=module_number,technique=technique)
        #conversations=list(set(conversations))
        return render(request,'conversationmanager/conversation_page.html',{'conversations': conversations,'user':request.user.get_username()})
    