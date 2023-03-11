from django import forms
from .models import *


class CreateCourseForm(forms.ModelForm):
    type_course = forms.ChoiceField(choices=Courses.CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = Courses
        fields = ['title', 'photo', 'type_course']

