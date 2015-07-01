from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Options)
admin.site.register(Dialogs)
admin.site.register(Userconversation)
admin.site.register(Conversationoptiongraph)
admin.site.register(Conversation)
admin.site.register(ConversationHistory)