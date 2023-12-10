from django import forms
from . import models

class RecipeForm(forms.ModelForm):
    class Meta:
        model = models.Recipe
        fields = ['name', 'description', 'ingredients', 'directions', 'image', 'category']
        labels = {'name': 'Recipe Name', 'description': 'Description', 'ingredients': 'Ingredients', 'directions': 'Directions', 'image': 'Image', 'category': 'Category'}
        