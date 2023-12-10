from django.urls import path
from . import views

app_name = 'recipes'

# Urls for the recipes application
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('recipes/<int:recipe_id>/', views.individual_recipe, name='individual_recipe'),
    path('recipes/new/', views.new_recipe, name='new_recipe'),
    path('recipes/<int:recipe_id>/edit/', views.edit_recipe, name='edit_recipe'),
    path('recieps/<int:recipe_id>/delete/', views.delete_recipe, name='delete_recipe'),
    path('categories/', views.categories, name='categoreis'),
]
