from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render,render_to_response , get_object_or_404 , get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect 
from django.core.urlresolvers import reverse
#from .forms import * 
from django.core import serializers
from django.views.decorators.cache import cache_control
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q , Max

def show_exercise_list(request):
    exercise_list=models.ExerciseConversation.objects.filter(conversation_type='Base')
    return render(request,'exercise/exercise_page.html',{'exercise_list':exercise_list})

def show_exercise(request):
    conversationID=request.POST.get('conversationid')
    conversation=models.ExerciseConversation.objects.get(conversationID=conversationID)
    return render(request,'exercise/conversation.html',{'conversation':conversation})

#----------------------------------------------------------------------
def conversation(request):
    conversation=models.ExerciseConversation.objects.get(conversationID=request.POST.get('conversationid'))
    technique=request.POST.get('technique')
    correct_technique=models.ConversationToModule.objects.get(conversation=conversation).correct_technique
    message=""
    try:
        next_conversation=models.ConversationToConversation.objects.get(base_conversation=conversation,technique=technique)
    except models.ConversationToConversation.DoesNotExist:
        message="no such technique"
        return  render(request,'exercise/conversation.html',{'conversation':conversation,'message':message})
    

    #return HttpResponse(next_conversation.technique_conversation.conversation_text)
    if correct_technique == technique:
        message=technique+" Great that worked. You helped the patient identify his/her NAT. see if there is any other technique as well "
    else:
        message="it looks like "+technique+" did not quite help the patient Identify the NAT. Go back and try a different technique. "
    return render(request,'exercise/done.html',{'conversation':conversation, 'next_conversation':next_conversation.technique_conversation,'message':message})

@user_passes_test(lambda u: u.is_superuser)
#----------------------------------------------------------------------
def exercise(request):
    last_conversation=models.ExerciseConversation.objects.all().aggregate(Max('conversationID'))['conversationID__max']
    #return HttpResponse(last_conversation)
    return render(request,"exercise/addexercise.html",{'last_conversation': last_conversation})
    
@user_passes_test(lambda u: u.is_superuser)
#----------------------------------------------------------------------
def add_exercise(request):
    base_conversation=request.POST.get('base_conversation',None)
    last_conversation=models.ExerciseConversation.objects.all().aggregate(Max('conversationID'))['conversationID__max']
    #return HttpResponse("done")
    if(last_conversation == None):
        last_conversation=0

    if not base_conversation == None:
        base=models.ExerciseConversation.objects.create(conversationID=last_conversation+1,conversation_text=base_conversation,conversation_type='Base')
        i=0
        while(not request.POST.get('technique[%d]' % i,None) == None):
            last_conversation=models.ExerciseConversation.objects.all().aggregate(Max('conversationID'))['conversationID__max']
            try:
                technique=models.ExerciseConversation.objects.create(conversationID=last_conversation+1,conversation_text=request.POST.get('technique_conversation[%d]' % i),conversation_type='Technique')
                models.ConversationToConversation.objects.create(base_conversation=base,technique=request.POST.get('technique[%d]' % i),technique_conversation=technique)
                if(not request.POST.get('is_correct[%d]' %i,None) == None):
                    models.ConversationToModule.objects.create(module_number=int(request.POST.get('module_number')),conversation=base,correct_technique=request.POST.get('technique[%d]' % i))
            except KeyError as e:
                return HttpResponse("error"+ e)
            i=i+1
        return HttpResponse("done")
    else:
        return HttpResponse("not done")
