from django import forms
from chat.models import ChatWithUser


class ChatForm(forms.ModelForm):
    model = ChatWithUser
    fields = ['text_message', ]