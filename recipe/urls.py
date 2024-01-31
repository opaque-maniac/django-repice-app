from django.urls import path
from .views import (
    all_recipes_view,
)

app_name = 'recipe'

# Path: recipe/urls.py
urlpatterns = [
    path('', all_recipes_view, name='all_recipes'),
]