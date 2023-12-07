from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from . import forms
from . import models

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=password)
            login(request, account)
            return redirect('account:edit_profile')
        else:
            context = { 'errors': form.errors, 'form': form }
            return render(request, 'account/register.html', context)
    else:
        form = forms.RegisterForm()
        context = { 'form': form }
        return render(request, 'account/register.html', context)
    
def login_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(email=email)
            account = authenticate(username=user.username, password=password)
            login(request, account)
            return redirect('recipe:index')
        else:
            context = { 'errors': form.errors, 'form': form }
            return render(request, 'account/login.html', context)
    else:
        form = forms.LoginForm()
        context = { 'form': form }
        return render(request, 'account/login.html', context)
    
# View for logout
def logout_view(request):
    auth_views.logout(request)
    return redirect('recipe:index')

# View for profile
@login_required
def profile(request):
    my_profile = UserProfile.objects.filter(user=request.user).first()
    context = { 'profile': my_profile }
    return render(request, 'account/profile.html', context)

# View for edit profile
@login_required
def edit_profile(request):
    profile = models.UserProfile.objects.filter(user=request.user).first()
    if profile.first_name.length > 0:
        new = False
    new = True
    if request.method == 'POST':
        form = forms.EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            if new:
                return redirect('recipe:index')
            return redirect('account:profile')
        else:
            context = { 'errors': form.errors, 'form': form }
            return render(request, 'account/edit_profile.html', context)
    else:
        form = forms.EditProfileForm(instance=profile)
        context = { 'form': form }
        return render(request, 'account/edit_profile.html', context)
