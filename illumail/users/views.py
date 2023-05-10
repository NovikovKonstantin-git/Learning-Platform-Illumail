from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, ListView
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cnt_sbs'] = len(CustomUser.objects.get(id=self.request.user.id).subscriptions.all())
        return context


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


class MySubscriptions(ListView):
    template_name = 'subscriptions.html'
    extra_context = {'title': 'Подписки', 'subtitle': 'Вы подписаны на:'}
    context_object_name = 'subscriptions'

    def get_queryset(self):
        return CustomUser.objects.get(id=self.request.user.id).subscriptions.all()


class AnotherUser(DetailView):
    model = CustomUser
    template_name = 'another_user.html'
    extra_context = {'title': 'Пользователь'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['another_user'] = CustomUser.objects.get(pk=self.kwargs['pk'])

        # чтобы появлялась кнопка подписаться/отписаться
        context['is_followed'] = False
        if CustomUser.objects.get(pk=self.kwargs['pk']) in CustomUser.objects.get(id=self.request.user.id).subscriptions.all():
            context['is_followed'] = True
        else:
            context['is_followed'] = False
        return context


def add_subscription(request, pk):
    CustomUser.objects.get(id=request.user.id).subscriptions.add(CustomUser.objects.get(id=pk))
    return HttpResponseRedirect(reverse('my_subscriptions', args=[request.user.id]))


def unsubscribe(request, pk):
    CustomUser.objects.get(id=request.user.id).subscriptions.remove(CustomUser.objects.get(id=pk))
    return HttpResponseRedirect(reverse('my_subscriptions', args=[request.user.id]))


class SearchUsers(ListView):
    model = CustomUser
    template_name = 'search_users.html'
    context_object_name = 'users'
    extra_context = {'title': 'Поиск пользователей', 'subtitle': 'По Вашему запросу найдено:'}

    def get_queryset(self):
        return CustomUser.objects.filter(username__icontains=self.request.GET.get('search', ''))