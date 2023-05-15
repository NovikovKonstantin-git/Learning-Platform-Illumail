from django import forms
from .models import CompletedTaskInStudyGroup


class ComplitedTaskGroupForm(forms.ModelForm):
    file = forms.FileField(label='Файл', widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = CompletedTaskInStudyGroup
        fields = ['file', ]
