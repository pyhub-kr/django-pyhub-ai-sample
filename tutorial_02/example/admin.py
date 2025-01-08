from django.contrib import admin
from .models import LLMChatRoom

@admin.register(LLMChatRoom)
class LLMChatRoomAdmin(admin.ModelAdmin):
    pass
