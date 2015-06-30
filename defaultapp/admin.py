from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(DefaultConversation)
admin.site.register(IntermediatebeliefConversation)
admin.site.register(CorebeliefConversation)
admin.site.register(PersistentnatConversation)
admin.site.register(EventlistConversation)