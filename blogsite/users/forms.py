from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class Userregisterform(UserCreationForm): #custom made form inherited from default form
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2'] #how the fields should be shown


class UserUpdateForm(forms.ModelForm): #ModelForm : form that work with specific database model
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']


class ProfileUpdateForm(forms.ModelForm):
   class Meta:
        model = Profile
        fields = ['image']