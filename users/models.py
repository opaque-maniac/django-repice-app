from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager

# Custom user model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Email"), unique=True)
    first_name = models.CharField(_("First name"), max_length=50)
    last_name = models.CharField(_("Last name"), max_length=50)
    profile_picture = models.ImageField(_("Profile picture"), upload_to="profile_pictures/", blank=True, null=True)
    is_staff = models.BooleanField(_("Staff status"), default=False)
    is_active = models.BooleanField(_("Active"), default=True)
    date_joined = models.DateTimeField(_("Date joined"), auto_now_add=True)
    last_login = models.DateTimeField(_("Last login"), auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']

    # Setting the custom user manager
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    # This method is required for the admin panel
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

