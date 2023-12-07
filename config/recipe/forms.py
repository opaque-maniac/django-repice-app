from django import forms
from . import models

# Form for adding a recipe
class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = models.Recipe
        fields = ['name', 'description', 'image', 'category']
        labels = {
            'name': '',
            'description': '',
            'image': '',
            'category': '',
            }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'add-recipe-input',
                'placeholder': 'Recipe Name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'add-recipe-input',
                'placeholder': 'Recipe Description',
            }),
            'image': forms.FileInput(attrs={
                'class': 'add-recipe-input',
                'placeholder': 'Recipe Image',
            }),
            'category': forms.Select(attrs={
                'class': 'add-recipe-input',
                'placeholder': 'Recipe Category',
            }),
        }

# Form for adding a comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['comment']
        labels = {
            'comment': '',
        }
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'comment-input',
                'placeholder': 'Add a comment',
            }),
        }