from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    username    = forms.CharField(max_length=120, required=True)
    first_name  = forms.CharField(max_length=100, required=True)
    surname     = forms.CharField(max_length=100, required=True)
    email       = forms.EmailField()
    password1   = forms.PasswordInput(attrs={'placeholder': 'Password'})
    password2   = forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'surname',
            'email',
            'password1',
            'password2'
        )
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
