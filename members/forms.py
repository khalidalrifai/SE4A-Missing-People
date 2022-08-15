from django import forms
from .models import Lost
from .models import Find

class ImageForm(forms.ModelForm):
    class Meta:
        model = Lost
        fields = '__all__'
        labels = {'photo':''}

class ImageForm2(forms.ModelForm):
    class Meta:
        model = Find
        fields = '__all__'
        labels = {'photo':''}
