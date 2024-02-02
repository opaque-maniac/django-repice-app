from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm
)
from django.utils.translation import gettext_lazy as _

# For for user registration
class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': _('Email'),
            'first_name': _('First name'),
            'last_name': _('Last name'),
            'password1': _('Password'),
            'password2': _('Confirm password')
        }
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control form__email',
                'placeholder': 'Email'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control form__first-name',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control form__last-name',
                'placeholder': 'Last name'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control form__password',
                'placeholder': 'Password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control form__password',
                'placeholder': 'Confirm password'
            })
        }

# Login form
class LoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password']
        labels = {
            'email': _('Email'),
            'password': _('Password')
        }
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control form__email',
                'placeholder': 'Email'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control form__password',
                'placeholder': 'Password'
            })
        }

# Form for updating user information
class UpdateUserForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'phone', 'address', 'city', 'country', 'profile_picture']
        labels = {
            'email': _('Email'),
            'first_name': _('First name'),
            'last_name': _('Last name'),
            'phone': _('Phone'),
            'address': _('Address'),
            'city': _('City'),
            'country': _('Country'),
            'profile_picture': _('Profile picture')
        }
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control form__email',
                'placeholder': 'Email'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control form__first-name',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control form__last-name',
                'placeholder': 'Last name'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control form__phone',
                'placeholder': 'Phone'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control form__address',
                'placeholder': 'Address'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control form__city',
                'placeholder': 'City'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control form__country',
                'placeholder': 'Country'
            }),
            'profile_picture': forms.FileInput(attrs={
                'class': 'form-control form__profile-picture'
            })
        }
        
