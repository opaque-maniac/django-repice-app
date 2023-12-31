from django.urls import path
from . import views

app_name = 'accounts'

# Urls for the accounts app
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<int:profile_id>/', views.other_profile, name='other_profile'),
]
