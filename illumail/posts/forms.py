from django import forms
from .models import *


class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'

