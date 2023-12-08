from functools import wraps
from django.shortcuts import get_list_or_404, redirect
from account.models import UserProfile

def user_not_blocked(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check if the user is blocked
        profile = UserProfile.objects.filter(user=request.user).first()
        if profile.is_blocked == True:
            return redirect('account:blocked')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
