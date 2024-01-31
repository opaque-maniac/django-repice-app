from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.urls import reverse

from .forms import RegisterForm, LoginForm

# View for the register page
def register_view(request):
    # If user is authenticated, redirect to home page
    if request.user.is_authenticated:
        return redirect(reverse('core:home'))
    
    # If request is POST, validate form and create user
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log user in and redirect to home page
            authenticated_user = authenticate(email=user.email, password=form.cleaned_data['password1'])
            login(request, authenticated_user)
            return redirect(reverse('core:home'))
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', { 'form': form })

# View for the login page
def login_view(request):
    # If user is authenticated, redirect to home page
    if request.user.is_authenticated:
        return redirect(reverse('core:home'))
    
    # If request is POST, validate form and log user in
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            # Log user in and redirect to home page
            login(request, user)
            return redirect(reverse('core:home'))
    else:
        form = LoginForm()
    return render(request, 'users/login.html', { 'form': form })

# View for the logout paged
def logout_view(request):
    logout(request)
    return redirect(reverse('core:home'))

# View for the profile page
def profile_view(request):
    profile = get_user_model().objects.get(pk=request.user.pk)
    return render(request, 'users/profile.html', { 'profile': profile })