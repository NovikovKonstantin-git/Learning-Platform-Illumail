from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from .forms import RegisterUser, UpdateProfileForm
from .models import CustomUser


def register_user(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('show_courses')
    else:
        form = RegisterUser()
    return render(request, 'register.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('show_courses')


def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('show_courses')
    return render(request, 'login.html')


def my_profile(request, id):
    profile = CustomUser.objects.get(id=id)
    return render(request, 'my_profile.html', {'profile': profile})


def update_profile(request, id):
    profile = CustomUser.objects.get(id=id)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('my_profile', id)
    return render(request, 'update_profile.html', {'form': form})