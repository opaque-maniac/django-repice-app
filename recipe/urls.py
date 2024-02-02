from django.urls import path
from .views import (
    all_recipes_view,
    recipe_detail_view,
    new_recipe_view,
    update_recipe_view,
)

app_name = 'recipe'

# Path: recipe/urls.py
urlpatterns = [
    path('all/', all_recipes_view, name='all_recipes'),
    path('new/', new_recipe_view, name='new_recipe'),
    path('<int:recipe_id>/', recipe_detail_view, name='recipe_detail'),
    path('<int:recipe_id>/update/', update_recipe_view, name='update_recipe'),
]
