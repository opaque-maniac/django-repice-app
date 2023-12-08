from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .decorators import user_not_blocked
from . import models
from . import forms

# View for the index page
def index(request):
    # Find last five recipes
    recipes = models.Recipe.objects.all().order_by('-id')[:5]
    context = { 'recipes': recipes }
    return render(request, 'recipe/index.html', context)

# View for the about page
def about(request):
    return render(request, 'recipe/about.html')

# View for the contact page
def contact(request):
    return render(request, 'recipe/contact.html')

# View for the categories page
@login_required
@user_not_blocked
def categories(request):
    categories = models.Category.objects.all()
    category_id = request.GET.get('category_id')

    if category_id:
        queryset = models.Recipe.objects.filter(category=category_id)
        paginator = Paginator(queryset, 10)  # 10 items per pag
        page = request.GET.get('page')
        try:
            paginated_data = paginator.page(page)
        except PageNotAnInteger:
            paginated_data = paginator.page(1)
        except EmptyPage:
            paginated_data = paginator.page(paginator.num_pages)
        context = { 'recipes': paginated_data, 'categories': categories }
        return render(request, 'recipes/all_recipes.html', context)
    else:
        recipes = models.Recipe.objects.all()[:5]
        context = { 'recipes': recipes, 'categories': categories }
    return render(request, 'recipe/categories.html', context)

# View for the recipe detail page
@login_required
@user_not_blocked
def recipe(request, recipe_id):
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
@user_not_blocked
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
@user_not_blocked
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(models.Recipe, pk=recipe_id)
    recipe.delete()
    return redirect('recipe:index')

# View to edit recipe
@login_required
@user_not_blocked
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

# View for the all recipes page
@login_required
@user_not_blocked
def all_recipes(request):
    queryset = models.Recipe.objects.all()
    paginator = Paginator(queryset, 10)  # 10 items per page

    page = request.GET.get('page')
    try:
        paginated_data = paginator.page(page)
    except PageNotAnInteger:
        paginated_data = paginator.page(1)
    except EmptyPage:
        paginated_data = paginator.page(paginator.num_pages)

    return render(request, 'recipes/all_recipes.html', {'paginated_data': paginated_data})

# View for the recipe search result page
@login_required
@user_not_blocked
def recipe_search(request):
    if request.method == 'POST':
        search = request.POST['search']
        queryset = models.Recipe.objects.filter(name__icontains=search)
        paginator = Paginator(queryset, 10)  # 10 items per page

        page = request.GET.get('page')
        try:
            paginated_data = paginator.page(page)
        except PageNotAnInteger:
            paginated_data = paginator.page(1)
        except EmptyPage:
            paginated_data = paginator.page(paginator.num_pages)
        context = { 'recipes': paginated_data }
        return render(request, 'recipe/recipe_search.html', context)
    else:
        return redirect('recipe:all_recipes')
