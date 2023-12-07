from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from . import models

# Form for registration
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
        widget = {
            'email': forms.EmailInput(attrs={
                'class': 'register-input',
                'placeholder': 'Email'
            }),
            'username': forms.TextInput(attrs={
                'class': 'register-input',
                'placeholder': 'Username',
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'register-input',
                'placeholder': 'Password',
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'register-input',
                'placeholder': 'Confirm Password',
            }),
        }

# Form for login
class LoginForm:
    class Meta:
        model = User
        fields = ['email', 'password']
        labels = {
            'email': '',
            'password': '',
            }
        widget = {
            'email': forms.EmailInput(attrs={
                'class': 'login-input',
                'placeholder': 'Email'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'login-input',
                'placeholder': 'Password',
            }),
        }

# Form for editing profile
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = ['first_name', 'last_name', 'bio', 'profile_picture']
        labels = {
            'first_name': '',
            'last_name': '',
            'bio': '',
            'profile_picture': '',
            }
        widget = {
            'first_name': forms.TextInput(attrs={
                'class': 'edit-profile-input',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'edit-profile-input',
                'placeholder': 'Last Name',
            }),
            'bio': forms.TextInput(attrs={
                'class': 'edit-profile-input',
                'placeholder': 'Bio',
            }),
            'profile_picture': forms.FileInput(attrs={
                'class': 'edit-profile-input',
                'placeholder': 'Profile Picture',
            }),
        }