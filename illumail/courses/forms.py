from django import forms
from .models import CompletedTaskModel


class ComplitedTaskForm(forms.ModelForm):
    file = forms.FileField(label='Файл', widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = CompletedTaskModel
        fields = ['file', ]
