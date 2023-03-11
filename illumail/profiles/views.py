from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from.forms import *


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        form_profile = ProfileForm(request.POST)
        if form.is_valid() and form_profile.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            userobj = User.objects.get(username=username)

            first_name = form_profile.cleaned_data['first_name']
            last_name = form_profile.cleaned_data['last_name']
            patronymic = form_profile.cleaned_data['patronymic']

            Profile.objects.create(user=userobj, first_name=first_name, last_name=last_name, patronymic=patronymic)

            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('show_all_courses')
    else:
        form = RegisterUserForm()
        form_profile = ProfileForm()
    return render(request, 'register.html', {'form': form, 'form_profile': form_profile})


def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('show_all_courses')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('show_all_courses')


def my_profile(request, user_id):
    profiles = Profile.objects.get(user=user_id)
    return render(request, 'my_profile.html', {'profiles': profiles})
