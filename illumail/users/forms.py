from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser


class RegisterUser(UserCreationForm):
    first_name = forms.CharField(label='Имя:', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия:', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    patronymic = forms.CharField(label='Отчество:', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    email = forms.EmailField(label='Эл.почта:', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    username = forms.CharField(label='Имя пользователя:', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль:', required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля:', required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'patronymic', 'email', 'username', 'password1', 'password2')


class UpdateProfileForm(forms.ModelForm):
    bio = forms.CharField(label='О себе', widget=forms.TextInput(attrs={'placeholder': 'О себе...'}))

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'patronymic', 'photo', 'email', 'username', 'bio', 'password',)
