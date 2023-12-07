from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.contrib.auth.decorators import login_required

from . import models
from . import forms
from account.models import UserProfile

# View for the index page
def index(request):
    # Find last five recipes
    recipes = models.Recipe.objects.all().order_by('-id')[:5]
    context = { 'recipes': recipes }
    return render(request, 'recipe/index.html', context)

# View for the recipe detail page
@login_required
def repice(request, recipe_id):
    recipe = get_object_or_404(models.Recipe, pk=recipe_id)
    comments = get_list_or_404(models.Comment, recipe=recipe_id)

    # If request method is post
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe:recipe', args=[int(recipe_id)])
        else:
            context = { 'recipe': recipe, 'comments': comments, 'form': form, 'errors': form.errors }
            return render(request, 'recipe/recipe.html', context)
    else:
        form = forms.CommentForm()
    context = { 'recipe': recipe, 'comments': comments }
    return render(request, 'recipe/recipe.html', context)

# View to add recipe
@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = forms.AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('recipe:index')
        else:
            context = { 'form': form, 'errors': form.errors }
            return render(request, 'recipe/add_recipe.html', context)
    else:
        form = forms.AddRecipeForm()
    context = { 'form': form }
    return render(request, 'recipe/add_recipe.html', context)

# View to delete recipe
@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(models.Recipe, pk=recipe_id)
    recipe.delete()
    return redirect('recipe:index')

# View to edit recipe
@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(models.Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = forms.AddRecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe:recipe', args=[int(recipe_id)])
        else:
            context = { 'form': form, 'errors': form.errors }
            return render(request, 'recipe/edit_recipe.html', context)
    else:
        form = forms.AddRecipeForm(instance=recipe)
    context = { 'form': form }
    return render(request, 'recipe/edit_recipe.html', context)