from django import forms
from django.contrib.auth.models import User
from .models import Test, Questions

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields= ['title']
        
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['title', 'question', 'a1', 'a2', 'a3', 'a4', 'answer', 'marks']