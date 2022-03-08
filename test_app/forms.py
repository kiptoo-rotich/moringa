from .models import School
from django import forms
class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'
