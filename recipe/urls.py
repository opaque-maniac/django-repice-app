from django.urls import path
from .views import (
    all_recipes_view,
    recipe_detail_view,
    new_recipe_view,
    update_recipe_view,
    delete_recipe_view,
    user_recipes_view,
    explore,
)

app_name = 'recipe'

# Path: recipe/urls.py
urlpatterns = [
    path('all/', all_recipes_view, name='all_recipes'),
    path('new/', new_recipe_view, name='new_recipe'),
    path('<int:recipe_id>/', recipe_detail_view, name='recipe_detail'),
    path('<int:recipe_id>/update/', update_recipe_view, name='update_recipe'),
    path('<int:recipe_id>/delete/', delete_recipe_view, name='delete_recipe'),
    path('user/<int:user_id>/', user_recipes_view, name='user_recipes'),
    path('explore/', explore, name="explore"),
]
