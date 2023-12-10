from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from . import models
from . import forms

# View for the index page
def index(request):
    recipes = models.Recipe.objects.all()[:5]
    context = { 'recipes': recipes }
    return render(request, 'recipes/index.html', context)

# View for the about page
def about(request):
    return render(request, 'recipes/about.html')

# View for the contact page
def contact(request):
    return render(request, 'recipes/contact.html')

# View for individual recipe
@login_required
def individual_recipe(request, recipe_id):
    recipe = models.Recipe.objects.filter(pk=recipe_id)
    context = { 'recipe': recipe }
    return render(request, 'recipes/individual_recipe.html', context)

# View for the explore page
@login_required
def categories(request):
    categories = models.Category.objects.all()
    category_id = request.GET.get('category_id')
    query = request.GET.get('query')

    recipes = models.Recipe.objects.all()[:5]

    if category_id:
        category_selected = models.Category.objects.filter(pk=category_id)
        recipes = models.Recipe.objects.filter(category = category_selected)
        context = { 'categories': categories, 'recipes': recipes, 'selected_category': category_selected }
    elif query:
        recipes = models.Recipe.objects.filter(name__contains=query)
        context = { 'categories': categories, 'recipes': recipes }
    else:
        context = { 'categories': categories, 'recipes': recipes }

    return render(request, 'recipes/categories.html', context) 

# View for the new recipe page
@login_required
def new_recipe(request):
    if request.method == 'POST':
        form = forms.RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('recipes:individual_recipe', args=[int(recipe.id)])
        else:
            form.add_error(None, 'Error when saving new recipe')
            context = { 'errors': form.errors, 'form': form, 'new': True }
    else:
        form = forms.RecipeForm()
    context = { 'form': form, 'new': True }
    return render(request, 'recipes/new_recipe.html', context)

# View for edit recipe function
@login_required
def edit_recipe(request, recipe_id):
    recipe = models.Recipe.objects.filter(pk=recipe_id)
    if request.user != recipe.user:
        raise Http404
    if request.method == 'POST':
        form = forms.RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes:individual_recipe', args=[int(recipe.id)])
        else:
            form.add_error(None, 'Error when eding recipe')
            context = { 'errors': form.errors, 'form': form, 'new': False }
            return render(request, 'recipes/new_recipe', context)
    else:
        form = forms.RecipeForm(instance=recipe)
    context = { 'form': form, 'new': False }
    return render(request, 'recipes/new_recipe', context)

# View for delete recipe
@login_required
def delete_recipe(request, recipe_id):
    recipe = models.Recipe.objects.filter(pk=recipe_id)
    if request.user != recipe.user:
        raise Http404
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes:index')
    return render(request, 'recipes/delete_recipe.html', { 'recipe': recipe })

