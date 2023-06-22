from django.contrib import admin
from chat.models import ChatWithUser


class ChatAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'text_message', 'date_message')


admin.site.register(ChatWithUser, ChatAdmin)
