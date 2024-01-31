from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Recipe

# View for all the recipes page
def all_recipes_view(request):
    all_recipes = Recipe.objects.all()
    items_per_page = 15
    paginator = Paginator(all_recipes, items_per_page)
    page = request.GET.get('page')
    try:
        # Get objects for the given page
        recipes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        recipes = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        recipes = paginator.page(paginator.num_pages)

    return render(request, 'recipe/all_recipes.html', { 'recipes': recipes })
