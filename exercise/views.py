
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render,render_to_response , get_object_or_404 , get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect 
from django.core.urlresolvers import reverse
from django.core import serializers
from django.views.decorators.cache import cache_control
from datetime import datetime
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import models , forms
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q , Max

@login_required(login_url='/accounts/login/')
def show_exercise_list(request):
    exercise_list=models.ExerciseConversation.objects.filter(conversation_type='Base')
    return render(request,'exercise/exercise_page.html',{'exercise_list':exercise_list})

@login_required(login_url='/accounts/login/')
def show_exercise(request):
    conversationID=request.POST.get('conversationid')
    # module number to be used for setting messages specific to a module
    module_number=request.POST.get('module_number')
    #return HttpResponse(module_number)    
    conversation=models.ExerciseConversation.objects.get(conversationID=conversationID)
    return render(request,'exercise/exercise_conversation.html',{'conversation':conversation,'module_number':module_number})

#----------------------------------------------------------------------
@login_required(login_url='/accounts/login/')
def conversation(request):
    conversation=models.ExerciseConversation.objects.get(conversationID=request.POST.get('conversationid'),conversation_type="Base")
    message=""
    try:
        technique=models.Technique.objects.get(technique_text=request.POST.get('technique'))
        #return HttpResponse(conversation)
        next_conversation=get_object_or_404(models.ConversationToConversation,base_conversation=conversation,technique=technique)
        
        correct_techniques=models.ConversationToModule.objects.filter(conversationID=conversation).values_list('correct_technique',flat=True).distinct()
        #return HttpResponse(technique.technique_id in correct_techniques)
        if technique.technique_id in correct_techniques:
            message=technique.technique_text +" Great that worked. You helped the patient identify his/her NAT. see if there is any other technique as well "
            return render(request,'exercise/exercise_conversation.html',{'conversation':conversation, 'next_conversation':next_conversation.technique_conversation,'message':message})
            
        message="it looks like "+technique.technique_text+" did not quite help the patient Identify the NAT. Go back and try a different technique. "
        return render(request,'exercise/exercise_conversation.html',{'conversation':conversation, 'next_conversation':next_conversation.technique_conversation,'message':message})        
    except models.Technique.DoesNotExist:
        message="technique does not exists"
        return  render(request,'exercise/exercise_conversation.html',{'conversation':conversation,'message':message})
    

@user_passes_test(lambda u: u.is_superuser)
#----------------------------------------------------------------------
def exercise(request):
    return render(request,"exercise/addexercise.html")
    
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
                technique=models.Technique.objects.get(module_number=int(request.POST.get('module_number')),technique_text=request.POST.get('technique[%d]' % i))
            except models.Technique.DoesNotExist:
                last_technique=models.Technique.objects.all().aggregate(Max('technique_id'))['technique_id__max']
                technique=models.Technique.objects.create(technique_id=last_technique+1,module_number=int(request.POST.get('module_number')),technique_text=request.POST.get('technique[%d]' % i))
            try:
                technique_conversation =models.ExerciseConversation.objects.create(conversationID=last_conversation+1,conversation_text=request.POST.get('technique_conversation[%d]' % i),conversation_type='Technique')
                models.ConversationToConversation.objects.get_or_create(base_conversation=base,technique=technique,technique_conversation=technique_conversation)
                if(not request.POST.get('is_correct[%d]' %i,None) == None):
                    models.ConversationToModule.objects.get_or_create(module_number=int(request.POST.get('module_number')),conversationID=base,correct_technique=technique)
            except KeyError as e:
                return HttpResponse("error"+ e)
            i=i+1
        return render(request, "exercise/added.html",{'base':base})
    else:
        return HttpResponse("not done")

"""
@login_required(login_url='/accounts/login/')
#----------------------------------------------------------------------
def identify_nat(request):
    if request.method == 'GET':
        form=forms.Identifynatform()
    else:
        form=forms.Identifynatform(request.POST)
        if form.is_valid():
            form.save(request)
            return HttpResponse("done")
    return render(request,'exercise/identifynatform.html',{'form':form})
        
@login_required(login_url='/accounts/login/')
#----------------------------------------------------------------------
def challenge_nat(request):
    if request.method == 'GET':
        form=forms.Challengenatform()
    else:
        form=forms.Challengenatform(request.POST)
        if form.is_valid():
            form.save(request)
            return HttpResponse('done')
    return render(request,'exercise/challengenatform.html',{'form':form})

@login_required(login_url='/accounts/login/')
#----------------------------------------------------------------------
@login_required(login_url='/accounts/login/')
def modifybeliefs(request):
    if request.method == 'GET':
        form=forms.Modifyingbeliefform()
    else:
        form=forms.Modifyingbeliefform(request.POST)
        if form.is_valid():
            form.save(request)
            return HttpResponse('done')
    return render(request,'exercise/modifybeliefsform.html',{'form':form})
    
"""