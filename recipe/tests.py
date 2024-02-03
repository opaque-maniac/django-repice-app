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
        self.user.save()

        self.recipe_data = {
            'author': self.user,
            'title': 'Test Recipe',
            'category': 'Breakfast',
            'description': 'A test recipe',
            'content': 'This is a test recipe'
        }
        self.recipe = Recipe.objects.create(**self.recipe_data)
        self.recipe.save()
    
    def test_create_recipe(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.author, self.user)
        self.assertEqual(recipe.title, self.recipe_data['title'])
        self.assertEqual(recipe.category, self.recipe_data['category'])
        self.assertEqual(recipe.description, self.recipe_data['description'])
        self.assertEqual(recipe.content, self.recipe_data['content'])
        self.assertEqual(recipe.date_created, self.recipe.date_created)
        self.assertEqual(recipe.date_updated, self.recipe.date_updated)

    def test_recipe_str(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(str(recipe), self.recipe_data['title'])
    
    def tearDown(self):
        self.recipe.delete()
        self.user.delete()


# Tests for the all reciepes view
class TestAllRecipesView(TestCase):
    def setUp(self):
        self.credentials = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.credentials)
        self.user.save()
        
        self.recipe_data = {
            'author': self.user,
            'title': 'Test Recipe',
            'category': 'Breakfast',
            'description': 'A test recipe',
            'content': 'This is a test recipe'
        }
        self.recipe = Recipe.objects.create(**self.recipe_data)
        self.recipe.save()
    
    def test_response_code(self):
        response = self.client.get('/recipe/all/')
        self.assertEqual(response.status_code, 302)
    
    def test_response_code_name(self):
        response = self.client.get(reverse('recipe:all_recipes'))
        self.assertEqual(response.status_code, 302)
    
    def test_redirect(self):
        response = self.client.get(reverse('recipe:all_recipes'))
        self.assertRedirects(response, '/users/login/?next=/recipe/all/')
    
    def test_response_code_authenticated(self):
        self.client.login(email=self.credentials['email'], password=self.credentials['password'])
        response = self.client.get(reverse('recipe:all_recipes'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_used(self):
        self.client.login(email=self.credentials['email'], password=self.credentials['password'])
        response = self.client.get(reverse('recipe:all_recipes'))
        self.assertTemplateUsed(response, 'recipe/all_recipes.html')

    def tearDown(self):
        self.recipe.delete()
        self.user.delete()

# Tests for the recipe detail view
class TestRecipeDetailView(TestCase):
    def setUp(self):
        self.credentials = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.credentials)
        self.user.save()
        
        self.recipe_data = {
            'author': self.user,
            'title': 'Test Recipe',
            'category': 'Breakfast',
            'description': 'A test recipe',
            'content': 'This is a test recipe'
        }
        self.recipe = Recipe.objects.create(**self.recipe_data)
        self.recipe.save()
    
    def test_response_code(self):
        response = self.client.get('/recipe/1/')
        self.assertEqual(response.status_code, 302)
    
    def test_response_code_name(self):
        response = self.client.get(reverse('recipe:recipe_detail', args=[1]))
        self.assertEqual(response.status_code, 302)
    
    def test_redirect(self):
        response = self.client.get(reverse('recipe:recipe_detail', args=[1]))
        self.assertRedirects(response, '/users/login/?next=/recipe/1/')
    
    def test_response_code_authenticated(self):
        self.client.login(email=self.credentials['email'], password=self.credentials['password'])
        response = self.client.get(reverse('recipe:recipe_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
    
    def test_template_used(self):
        self.client.login(email=self.credentials['email'], password=self.credentials['password'])
        response = self.client.get(reverse('recipe:recipe_detail', args=[1]))
        self.assertTemplateUsed(response, 'recipe/recipe_detail.html')
    
    def tearDown(self):
        self.recipe.delete()
        self.user.delete()

# Tests for the new recipe view
class TestNewRecipeView(TestCase):
    def setUp(self):
        self.credentials = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.credentials)
        self.user.save()
        
        self.recipe_data = {
            'author': self.user,
            'title': 'Test Recipe',
            'category': 'Breakfast',
            'description': 'A test recipe',
            'content': 'This is a test recipe'
        }
        self.recipe = Recipe.objects.create(**self.recipe_data)
        self.recipe.save()
    
    def test_response_code(self):
        response = self.client.get('/recipe/new/')
        self.assertEqual(response.status_code, 302)
    
    def test_response_code_name(self):
        response = self.client.get(reverse('recipe:new_recipe'))
        self.assertEqual(response.status_code, 302)
    
    def test_redirect(self):
        response = self.client.get(reverse('recipe:new_recipe'))
        self.assertRedirects(response, '/users/login/?next=/recipe/new/')
    
    def test_response_code_authenticated(self):
        self.client.login(email=self.credentials['email'], password=self.credentials['password'])
        response = self.client.get(reverse('recipe:new_recipe'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_used(self):
        self.client.login(email=self.credentials['email'], password=self.credentials['password'])
        response = self.client.get(reverse('recipe:new_recipe'))
        self.assertTemplateUsed(response, 'recipe/new_recipe.html')
    
    def tearDown(self):
        self.recipe.delete()
        self.user.delete()

# Tests for the update recipe view
class TestUpdateRecipeView(TestCase):
    def setUp(self):
        self.credentials = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.credentials)
        self.user.save()
    
        self.credentials2 = {
            'email': 'test2@example.com',
            'first_name': 'Test2',
            'last_name': 'User2',
            'password': 'testpassword2'
        }
        self.user2 = get_user_model().objects.create_user(**self.credentials2)
        self.user2.save()
        
        self.recipe_data = {
            'author': self.user,
            'title': 'Test Recipe',
            'category': 'Breakfast',
            'description': 'A test recipe',
            'content': 'This is a test recipe'
        }
        self.recipe = Recipe.objects.create(**self.recipe_data)
        self.recipe.save()
    
    def test_response_code(self):
        response = self.client.get('/recipe/1/update/')
        self.assertEqual(response.status_code, 302)
    
    def test_response_code_name(self):
        response = self.client.get(reverse('recipe:update_recipe', args=[1]))
        self.assertEqual(response.status_code, 302)
    
    def test_redirect(self):
        response = self.client.get(reverse('recipe:update_recipe', args=[1]))
        self.assertRedirects(response, '/users/login/?next=/recipe/1/update/')
    
    def test_response_code_authenticated(self):
        self.client.login(email=self.credentials['email'], password=self.credentials['password'])
        response = self.client.get(reverse('recipe:update_recipe', args=[1]))
        self.assertEqual(response.status_code, 200)
    
    def test_owner_restrictions(self):
        self.client.login(email=self.credentials2['email'], password=self.credentials2['password'])
        response = self.client.get(reverse('recipe:update_recipe', args=[1]))
        self.assertEqual(response.status_code, 404)
    
    def test_template_used(self):
        self.client.login(email=self.credentials['email'], password=self.credentials['password'])
        response = self.client.get(reverse('recipe:update_recipe', args=[1]))
        self.assertTemplateUsed(response, 'recipe/update_recipe.html')
    
    def tearDown(self):
        self.recipe.delete()
        self.user.delete()
        self.user2.delete()

# Tests for the delete recipe view
class TestDeleteRecipeView(TestCase):
    def setUp(self):
        self.credentials = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.credentials)
        self.user.save()
    
        self.credentials2 = {
            'email': 'test2@example.com',
            'first_name': 'Test2',
            'last_name': 'User2',
            'password': 'testpassword2'
        }
        self.user2 = get_user_model().objects.create_user(**self.credentials2)
        self.user2.save()
        
        self.recipe_data = {
            'author': self.user,
            'title': 'Test Recipe',
            'category': 'Breakfast',
            'description': 'A test recipe',
            'content': 'This is a test recipe'
        }
        self.recipe = Recipe.objects.create(**self.recipe_data)
    
    def test_response_code(self):
        response = self.client.get('/recipe/1/delete/')
        self.assertEqual(response.status_code, 302)
    
    def test_response_code_name(self):
        response = self.client.get(reverse('recipe:delete_recipe', args=[1]))
        self.assertEqual(response.status_code, 302)
    
    def test_redirect(self):
        response = self.client.get(reverse('recipe:delete_recipe', args=[1]))
        self.assertRedirects(response, '/users/login/?next=/recipe/1/delete/')
    
    def test_response_code_authenticated(self):
        self.client.login(email=self.credentials['email'], password=self.credentials['password'])
        response = self.client.get(reverse('recipe:delete_recipe', args=[1]))
        self.assertEqual(response.status_code, 302)
    
    def test_owner_restrictions(self):
        self.client.login(email=self.credentials2['email'], password=self.credentials2['password'])
        response = self.client.get(reverse('recipe:delete_recipe', args=[1]))
        self.assertEqual(response.status_code, 404)
    
    def tearDown(self):
        self.recipe.delete()
        self.user.delete()
        self.user2.delete()

# Tests for the user recipes view
class TestUserRecipesView(TestCase):
    def setUp(self):
        self.credentials = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.credentials)
        self.user.save()
        
        self.recipe_data1 = {
            'author': self.user,
            'title': 'Test Recipe',
            'category': 'Breakfast',
            'description': 'A test recipe',
            'content': 'This is a test recipe'
        }
        self.recipe1 = Recipe.objects.create(**self.recipe_data1)
        self.recipe1.save()

        self.recipe_data2 = {
            'author': self.user,
            'title': 'Test Recipe 2',
            'category': 'Breakfast',
            'description': 'A test recipe 2',
            'content': 'This is a test recipe 2'
        }
        self.recipe2 = Recipe.objects.create(**self.recipe_data2)
        self.recipe2.save()
    
    def test_response_code(self):
        response = self.client.get('/recipe/user/1/')
        self.assertEqual(response.status_code, 302)
    
    def test_response_code_name(self):
        response = self.client.get(reverse('recipe:user_recipes', args=[1]))
        self.assertEqual(response.status_code, 302)
    
    def test_redirect(self):
        response = self.client.get(reverse('recipe:user_recipes', args=[1]))
        self.assertRedirects(response, '/users/login/?next=/recipe/user/1/')

    def test_response_code_authenticated(self):
        self.client.login(email=self.credentials['email'], password=self.credentials['password'])
        response = self.client.get(reverse('recipe:user_recipes', args=[1]))
        self.assertEqual(response.status_code, 200)
    
    def test_template_used(self):
        self.client.login(email=self.credentials['email'], password=self.credentials['password'])
        response = self.client.get(reverse('recipe:user_recipes', args=[1]))
        self.assertTemplateUsed(response, 'recipe/user_recipes.html')
    
    def tearDown(self):
        self.recipe1.delete()
        self.recipe2.delete()
        self.user.delete() 
    