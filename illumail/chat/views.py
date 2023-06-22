# chat/views.py
from django.http import HttpResponseRedirect
from django.shortcuts import render
from chat.forms import ChatForm
from chat.models import ChatWithUser


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})