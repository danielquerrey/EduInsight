from django import forms
from myapp.models import TeachersClass

class TeachersClassForm(forms.ModelForm):
    class Meta:
        model = TeachersClass
        fields = ['class_name', 'teacher_name']