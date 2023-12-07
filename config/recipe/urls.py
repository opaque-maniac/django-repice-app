from django.urls import path

from . import views

app_name = 'recipe'

# Urls for the recipe applicaton
urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/<int:recipe_id>/', views.recipe, name='recipe'),
    path('recipe/new/', views.add_recipe, name='add_recipe'),
    path('recipe/<int:recipe_id>/delete/', views.delete_recipe, name='delete_recipe'),
    path('recipe/<int:recipe_id>/edit/', views.edit_recipe, name='edit_recipe'),
]
