"""integrate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/',include('cbt2.urls',namespace='cbt2')),
    url(r'^home/','cbt2.views.home'),
    url(r'^welcome/','cbt2.views.welcome'),
    url(r'^fill/details/$','cbt2.views.user_details'),
    url(r'^fill/family_details/$','cbt2.views.family_details'),
    url(r'^signup/$','cbt2.views.usersignup'),
    url(r'^user/setting/$','cbt2.views.settings'),
    url(r'^accounts/login/$', 'cbt2.views.login'),
    url(r'^accounts/auth/$', 'cbt2.views.auth_view'),
    url(r'^accounts/logout/$', 'cbt2.views.logout'),
    url(r'^accounts/loggedin/$', 'cbt2.views.loggedin'),
    url(r'^accounts/invalid/$', 'cbt2.views.invalid_login'),
    url(r'^depression_quiz/submit/$','cbt2.views.set_depression_score'),
    url(r'^anxiety_quiz/submit/$','cbt2.views.set_anxiety_score'),    
    url(r'^depression_quiz/$','cbt2.views.show_depressionquiz'),
    url(r'^anxiety_quiz/$','cbt2.views.show_anxietyquiz'),
    url(r'^conversation/$','conversationmanager.views.carry_out_conversation'),
    #url(r'^conversation_page/','conversationmanager.views.conversation_page'),
    url(r'^add/conversations/$','conversationmanager.views.conversation'),
    url(r'^conversations/$','conversationmanager.views.add_conversation'),
    url(r'^admin_page/$','conversationmanager.views.admin'),
    url(r'^update/conversations/$','conversationmanager.views.update_conversation'),
    url(r'^edit/conversations/$','conversationmanager.views.edit_conversation'),
    url(r'^edit/conversations/done/$','conversationmanager.views.apply_update'),
    url(r'^exercise_page/$','exercise.views.show_exercise_list'),
    url(r'^exercise/$','exercise.views.show_exercise'),
    url(r'^exercise/conversation/$','exercise.views.conversation'),
    url(r'^add/exercises/$','exercise.views.exercise'),
    url(r'^add/exercises/done/$','exercise.views.add_exercise'),
    url(r'^module/$','defaultapp.views.modulemanager'),
    url(r'^Psychoeducation about Depression and CBT/technique/(?P<technique_id>[0-9]+)/$','psychoeducation.views.moduletechnique'),
    url(r'^history/$','conversationmanager.views.history'),
    url(r'^show/history/$','conversationmanager.views.show_history'),
    url(r'^Psychoeducation about Depression and CBT/show_list/$','psychoeducation.views.show_list'),
    url(r'^Psychoeducation about Depression and CBT/set_list/$','psychoeducation.views.set_list'),
    #url(r'^identifyNAT/$','exercise.views.identify_nat'),
    #url(r'^challengeNAT/$','exercise.views.challenge_nat'),
    #url(r'^modifybeliefs/$','exercise.views.modifybeliefs'),
    url(r'^Psychoeducation about Depression and CBT/$','psychoeducation.views.homepage'),
    url(r'^Behavioral Activation/$','behavioralactivation.views.homepage'),
    url(r'^Behavioral Activation/show_list/$','behavioralactivation.views.show_list'),
    url(r'^Behavioral Activation/set_list/$','behavioralactivation.views.set_list'),
    url(r'^Behavioral Activation/technique/(?P<technique_id>[0-9]+)/$','behavioralactivation.views.moduletechnique'),
    url(r'^Behavioral Activation/activityschedule','behavioralactivation.views.save_useractivity'),
    url(r'^Identifying NATs/$','identifynat.views.homepage'),
    url(r'^Identifying NATs/show_list/$','identifynat.views.show_list'),
    url(r'^Identifying NATs/set_list/$','identifynat.views.set_list'),
    url(r'^Identifying NATs/technique/(?P<technique_id>[0-9]+)/$','identifynat.views.moduletechnique'),
    url(r'^Identifying NATs/identifyNAT/$','identifynat.views.identify_nat'),
    url(r'^Challenging NATs/$','challengenat.views.homepage'),
    url(r'^Challenging NATs/show_list/$','challengenat.views.show_list'),
    url(r'^Challenging NATs/set_list/$','challengenat.views.set_list'),
    url(r'^Challenging NATs/technique/(?P<technique_id>[0-9]+)/$','challengenat.views.moduletechnique'),
    url(r'^Challenging NATs/challengenat/$','challengenat.views.challenge_nat'),
    url(r'^Modifying Intermediate and Core Beliefs/$','modifybelief.views.homepage'),
    url(r'^Modifying Intermediate and Core Beliefs/show_list/$','modifybelief.views.show_list'),
    url(r'^Modifying Intermediate and Core Beliefs/set_list/$','modifybelief.views.set_list'),
    url(r'^Modifying Intermediate and Core Beliefs/technique/(?P<technique_id>[0-9]+)/$','modifybelief.views.moduletechnique'),
    url(r'^Modifying Intermediate and Core Beliefs/modifybelief/$','modifybelief.views.modifybeliefs'),
    url(r'^Relapse Prevention/$','relapseprevention.views.homepage'),
    url(r'^Relapse Prevention/show_list/$','relapseprevention.views.show_list'),
    url(r'^Relapse Prevention/set_list/$','relapseprevention.views.set_list'),
    url(r'^Relapse Prevention/technique/(?P<technique_id>[0-9]+)/$','relapseprevention.views.moduletechnique'),
    url(r'^forum/',include('supportgroup.urls',namespace="supportgroup")),

]
