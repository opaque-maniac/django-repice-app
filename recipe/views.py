from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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
def recipe_detail_view(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'recipe/recipe_detail.html', { 'recipe': recipe })

# View for new recipe page
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
def update_recipe_view(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POSTz, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save()
            recipe.save()
            return redirect(reverse('recipe:recipe_detail', args=[recipe.id]))
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe/update_recipe.html', { 'form': form, 'recipe': recipe })


