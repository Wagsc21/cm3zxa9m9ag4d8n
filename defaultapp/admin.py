
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(DefaultConversation)
admin.site.register(ShowTechniqueBeliefsEventsNats)
admin.site.register(ConversationTechniqueBeliefsEventsNats)
admin.site.register(Technique)
admin.site.register(UserConversationTechnique)
admin.site.register(ShownListToUser)
