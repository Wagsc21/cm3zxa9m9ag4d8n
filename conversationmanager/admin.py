from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Options)
admin.site.register(Conversations)
admin.site.register(Userconversation)
admin.site.register(Conversationoption)