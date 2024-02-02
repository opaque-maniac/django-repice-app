from django.test import TestCase
from .models import Recipe
from django.contrib.auth import get_user_model
from django.urls import reverse

# Tests for the recipe models
class TestRecipeModel(TestCase):
    def setUp(self):
        self.user_credentials = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.user_credentials)
        self.recipe_credentials = {
            'title': 'Test Recipe',
            'description': 'Test Description',
            'author': self.user
        }
        self.recipe = Recipe.objects.create(**self.recipe_credentials)
    
    def test_create_recipe(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.title, self.recipe_credentials['title'])
        self.assertEqual(recipe.description, self.recipe_credentials['description'])
        self.assertEqual(recipe.author, self.user)
        self.assertEqual(recipe.category, 'Breakfast')
        self.assertEqual(recipe.content, '')
        self.assertTrue(recipe.date_created)
        self.assertTrue(recipe.date_updated)
    
    def test_recipe_str(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(str(recipe), self.recipe_credentials['title'])
    
# Tests for the all recipe views
class TestAllRecipesView(TestCase):
    def setUp(self):
        self.user_credentials = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.user_credentials)
        self.recipe_credentials = {
            'title': 'Test Recipe',
            'description': 'Test Description',
            'author': self.user
        }
        self.recipe = Recipe.objects.create(**self.recipe_credentials)
    
    def test_response_code(self):
        response = self.client.get('/recipe/all/')
        self.assertEqual(response.status_code, 200)
    



