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
    url(r'^home/','cbt2.views.home'),
    url(r'^fill/details/$','cbt2.views.user_details'),
    url(r'^fill/family_details/$','cbt2.views.family_details'),
    url(r'^signup/$','cbt2.views.usersignup'),
    url(r'^user/setting/$','cbt2.views.settings'),
    url(r'^accounts/login/$', 'cbt2.views.login'),
    url(r'^accounts/auth/$', 'cbt2.views.auth_view'),
    url(r'^accounts/logout/$', 'cbt2.views.logout'),
    url(r'^accounts/loggedin/$', 'cbt2.views.loggedin'),
    url(r'^accounts/invalid/$', 'cbt2.views.invalid_login'),
    url(r'^depression_quiz/','cbt2.views.show_depressionquiz'),
    url(r'^anxiety_quiz/','cbt2.views.show_anxietyquiz'),
    url(r'^result/(?P<num>[0-9]+)$','cbt2.views.depression_score'),
    url(r'^corebeliefs/(?P<num>[0-9]+)$','cbt2.views.show_corebeliefs'),
    url(r'^intermediatebeliefs/(?P<num>[0-9]+)$','cbt2.views.show_intermediatebeliefs'),
    url(r'^corebelief/submit/(?P<num>[0-9]+)/$','cbt2.views.set_corebeliefs'),
    url(r'^intermediatebelief/submit/(?P<num>[0-9]+)/$','cbt2.views.set_intermediatebeliefs'),
    url(r'^persistentnats/(?P<num>[0-9]+)$','cbt2.views.show_persistentnats'),
    url(r'^persistentnat/submit/(?P<num>[0-9]+)/$','cbt2.views.set_persistentnats'),
    url(r'^events/(?P<num>[0-9]+)$','cbt2.views.show_events'),
    url(r'^event/submit/(?P<num>[0-9]+)/$','cbt2.views.set_events'),
    url(r'^conversation/$','conversationmanager.views.carry_out_conversation'),
    url(r'^conversation_page/','conversationmanager.views.conversation_page'),
    url(r'^add/conversations/$','conversationmanager.views.conversation'),
    url(r'^conversations/$','conversationmanager.views.add_conversation'),
    url(r'^admin_page/$','conversationmanager.views.admin'),
    url(r'^update/conversations/$','conversationmanager.views.update_conversation'),
    url(r'^edit/conversations/$','conversationmanager.views.edit_conversation'),
    url(r'^edit/conversations/done/$','conversationmanager.views.apply_update'),
    url(r'^exercise_page/$','exercise.views.show_exercise_list'),
    url(r'exercise/$','exercise.views.show_exercise'),
    url(r'exercise/conversation/$','exercise.views.conversation'),
    url(r'add/exercises/$','exercise.views.exercise'),
    url(r'add/exercises/done/$','exercise.views.add_exercise')
]
