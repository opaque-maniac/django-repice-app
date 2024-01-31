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
        help_texts = {
            'email': _('Required. Please enter a valid email address.'),
            'first_name': _('Required. Please enter your first name.'),
            'last_name': _('Required. Please enter your last name.'),
            'password1': _('Required. Please enter a password.'),
            'password2': _('Required. Please confirm your password.')
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
        help_texts = {
            'email': _('Required. Please enter your email address.'),
            'password': _('Required. Please enter your password.')
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
