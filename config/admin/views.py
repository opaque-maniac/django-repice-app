from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from recipe.models import Recipe
from recipe.models import Category
from recipe.models import Comment
from account.models import UserProfile

# View for the all profiles page
@login_required
def all_profiles(request):
    profiles = UserProfile.objects.all()
    context = { 'profiles': profiles }
    return render(request, 'account/all_profiles.html', context)
