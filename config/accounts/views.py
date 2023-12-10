from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.http import Http404

from . import models
from . import forms

# View for the register page
def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm()
        if form.is_valid():
            user = form.save()
            models.Profile.objects.create(user=user)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=password)
            login(request, account)
            return redirect('recipes:index')
        else:
            form.add_error(None, 'Error occured when registering')
            context = { 'errors': form.errors, 'form': form }
            return render(request, 'accounts/register.html', context)
    else:
        context = { 'form': forms.RegisterForm()}
    return render(request, 'accounts/register.html', context)

# View for the login page
def login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                user = User.objects.get(email=email)
                account = authenticate(username=user.username, password=password)
                login(request, account)
                return redirect('recipes:index')
            except User.DoesNotExist:
                form.add_error(None, 'Email does not exist')
                context = { 'errors': form.errors, 'form': form }
                return render(request, 'accounts/login.html', context)
        else:
            form.add_error(None, 'Error occured when logging in')
            context = { 'errors': form.errors, 'form': form }
            return render(request, 'accounts/login.html', context)
    else:
        context = { 'form': forms.LoginForm()}
    return render(request, 'accounts/login.html', context)

# View for the logout page
def logout(request):
    return auth_views.LoginView.as_view()(request)

# View for the profile page
@login_required
def profile(request):
    try:
        profile = models.Profile.objects.filter(user=request.user)
    except models.Profile.DoesNotExist:
        raise Http404('Profile does not exist')
    context = { 'profile': profile }
    return render(request, 'accounts/profile.html', context)

# View for the profile page
@login_required
def other_profile(request, profile_id):
    try:
        profile = models.Profile.objects.filter(pk=profile_id)
    except models.Profile.DoesNotExist:
        raise Http404('Profile does not exist')
    context = { 'profile': profile }
    return render(request, 'accounts/profile.html', context)

# view for the edit profile page
@login_required
def edit_profile(request):
    try:
        profile = models.Profile.objects.get(user=request.user)
    except models.Profile.DoesNotExist:
        raise Http404('Profile does not exist')
    if request.method == 'POST':
        form = forms.EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
        else:
            form.add_error(None, 'Error occured when editing profile')
            context = { 'errors': form.errors, 'form': form }
            return render(request, 'accounts/edit_profile.html', context)
    else:
        context = { 'form': forms.EditProfileForm(instance=profile) }
    return render(request, 'accounts/edit_profile.html', context)

# View for delete profile page
@login_required
def delete_profile(request):
    try:
        profile = models.Profile.objects.filter(user=request.user)
    except models.Profile.DoesNotExist:
        raise Http404('Profile does not exist')
    profile.delete()
    return redirect('recipe:index')