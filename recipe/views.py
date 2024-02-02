from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Recipe
from .forms import RecipeForm

# View for all the recipes page
def all_recipes_view(request):
    all_recipes = Recipe.objects.all().prefetch_related('images').all()[:1]
    recipes_per_page = 15
    paginator = Paginator(all_recipes, recipes_per_page)
    page = request.GET.get('page')
    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        recipes = paginator.page(1)
    except EmptyPage:
        recipes = paginator.page(paginator.num_pages)

    return render(request, 'recipe/all_recipes.html', { 'recipes': recipes })

# View for the recipe detail page
@login_required
def recipe_detail_view(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'recipe/recipe_detail.html', { 'recipe': recipe })

# View for new recipe page
@login_required
def new_recipe_view(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect(reverse('recipe:recipe_detail', args=[recipe.id]))
    else:
        form = RecipeForm()
    return render(request, 'recipe/new_recipe.html', { 'form': form })

# View for the edit recipe page
@login_required
def update_recipe_view(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)

    # If the user is not the author of the recipe, raise a 404
    if request.user != recipe.author:
        raise Http404('You are not the author of this recipe.')

    if request.method == 'POST':
        form = RecipeForm(request.POSTz, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save()
            recipe.save()
            return redirect(reverse('recipe:recipe_detail', args=[recipe.id]))
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe/update_recipe.html', { 'form': form, 'recipe': recipe })

# View for the delete recipe page
@login_required
def delete_recipe_view(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)

    # If the user is not the author of the recipe, raise a 404
    if request.user != recipe.author:
        raise Http404('You are not the author of this recipe.')
    
    recipe.delete()
    return redirect(reverse('recipe:all_recipes'))

# View for the user's recipes page
def user_recipes_view(request, user_id):
    user = get_user_model().objects.get(pk=user_id)
    user_recipes = Recipe.objects.filter(author=user.id)
    recipes_per_page = 6
    paginator = Paginator(user_recipes, recipes_per_page)
    page = request.GET.get('page')
    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        recipes = paginator.page(1)
    except EmptyPage:
        recipes = paginator.page(paginator.num_pages)
    return render(request, 'recipe/user_recipes.html', {
        'recipes': recipes,
        'profile': user,
    })

