from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'category', 'description', 'content', 'cover_image']
        labels = {
            'title': 'Title',
            'category': 'Category',
            'description': 'Description',
            'cover_image': 'Cover image'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form__title',
                'placeholder': 'Title'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control form__category'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control form__description',
                'placeholder': 'Description'
            }),
            'cover_image': forms.FileInput(attrs={
                'class': 'form-control form__cover-image'
            })
        }