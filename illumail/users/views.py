from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView
from .forms import RegisterUser, UpdateProfileForm, NewPasswordForm
from .models import CustomUser


class RegisterNewUser(CreateView):
    form_class = RegisterUser
    template_name = 'register.html'
    extra_context = {'title': 'Регистрация'}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('show_courses')


class LogoutUser(LogoutView):
    next_page = 'show_courses'


class LoginUser(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('show_courses')
    extra_context = {'title': 'Вход'}


class MyProfile(DetailView):
    model = CustomUser
    template_name = 'my_profile.html'
    context_object_name = 'profile'
    extra_context = {'title': 'Мой профиль'}

    def get_object(self, queryset=None):
        return self.request.user


class UpdateProfile(UpdateView):
    form_class = UpdateProfileForm
    template_name = 'update_profile.html'
    extra_context = {'title': 'Изменение профиля'}

    def get_object(self, queryset=None):
        return self.request.user


class NewPassword(PasswordChangeView):
    form_class = NewPasswordForm
    template_name = 'new_password.html'
    success_url = reverse_lazy('show_courses')
    extra_context = {'title': 'Смена пароля'}





