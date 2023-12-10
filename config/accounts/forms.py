from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from . import models

# Form for registering user
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        labels = {
            'email': '',
            'username': '',
            'password1': '',
            'password2': '',
        }
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'register-form-input email',
                'placeholder': 'Email'
            }),
            'username': forms.TextInput(attrs={
                'class': 'register-form-input username',
                'placeholder': 'username',
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'register-form-input password',
                'placeholder': 'Password',
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'register-form-input password',
                'placeholder': 'Confirm password',
            })
        }

# Form for login user
class LoginForm(forms.ModelForm):
    email = forms.EmailInput(max_length=100)
    password = forms.PasswordInput()

# Form for editing profile
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['first_name', 'last_name', 'bio', 'image']
        labels = {
            'first_name': '',
            'last_name': '',
            'bio': '',
            'image': '',
        }
        widget = {
            'first_name': forms.TextInput(attrs={
                'class': 'edit-profile-form-input first-name',
                'placeholder': 'First name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'edit-profile-form-input last-name',
                'placeholder': 'Last name',
            }),
            'bio': forms.Textarea(attrs={
                'class': 'edit-profile-form-input bio',
                'placeholder': 'Bio',
            }),
            'image': forms.FileInput(attrs={
                'class': 'edit-profile-form-input image',
                'placeholder': 'Image',
            })
        }