from django import forms
from forum.models import ForumCommunication, ForumSection, ForumSubsection


class CommForm(forms.ModelForm):
    comm_text = forms.CharField(label='Текст', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = ForumCommunication
        fields = ['comm_text', ]


class CreateSubsection(forms.Form):
    subection = forms.CharField(label='Название темы', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = ForumSubsection
        fields = ['subsection', ]