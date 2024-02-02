from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Testing the custom user model
class TestUserModel(TestCase):
    def setUp(self):
        self.user_credentials = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.user_credentials)
        self.superuser_credentials = {
            'email': 'super@example.com',
            'first_name': 'Super',
            'last_name': 'User',
            'password': 'superpassword'
        }
        self.super_user = get_user_model().objects.create_superuser(**self.superuser_credentials)
    
    def test_create_user(self):
        user = get_user_model().objects.get(id=1)
        self.assertEqual(user.email, self.user_credentials['email'])
        self.assertEqual(user.first_name, self.user_credentials['first_name'])
        self.assertEqual(user.last_name, self.user_credentials['last_name'])
        self.assertTrue(user.check_password(self.user_credentials['password']))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        super_user = get_user_model().objects.get(id=2)
        self.assertEqual(super_user.email, self.superuser_credentials['email'])
        self.assertEqual(super_user.first_name, self.superuser_credentials['first_name'])
        self.assertEqual(super_user.last_name, self.superuser_credentials['last_name'])
        self.assertTrue(super_user.check_password(self.superuser_credentials['password']))
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)
    
    def test_user_str(self):
        user = get_user_model().objects.get(id=1)
        self.assertEqual(str(user), f'{user.id} : {self.user_credentials["first_name"]} {self.user_credentials["last_name"]}')


# Test the login page view
class TestLoginView(TestCase):
    def setUp(self):
        self.credentials = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.credentials)

    def test_response_code(self):
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)
    
    def test_response_code_name(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_used(self):
        response = self.client.get(reverse('users:login'))
        self.assertTemplateUsed(response, 'users/login.html')
    
    def test_login(self):
        response = self.client.post(reverse('users:login'), self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)

# Test for the register page view
class TestRegisterView(TestCase):
    def setUp(self):
        self.credentials = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpassword'
        }

    def test_response_code(self):
        response = self.client.get('/users/register/')
        self.assertEqual(response.status_code, 200)
    
    def test_response_code_name(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_used(self):
        response = self.client.get(reverse('users:register'))
        self.assertTemplateUsed(response, 'users/register.html')

    def test_register(self):
        response = self.client.post(reverse('users:register'), self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)

# Test for the logout page view
class TestLogoutView(TestCase):
    def setUp(self):
        self.credentials = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.credentials)
    
    def test_response_code(self):
        response = self.client.get('/users/logout/')
        self.assertEqual(response.status_code, 302)
    
    def test_response_code_name(self):
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)

# Test for the profile page view
class TestProfileView(TestCase):
    def setUp(self):
        self.credentials = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.credentials)
    
    def test_response_code(self):
        response = self.client.get('/users/profile/')
        self.assertEqual(response.status_code, 302)
    
    def test_response_code_name(self):
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 302)

    def test_redirect(self):
        response = self.client.get(reverse('users:profile'))
        self.assertRedirects(response, '/users/login/?next=/users/profile/')

# Test for the edit profile page view
class TestEditProfileView(TestCase):
    def setUp(self):
        self.credentials = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.credentials)
    
    def test_response_code(self):
        response = self.client.get('/users/profile/edit/')
        self.assertEqual(response.status_code, 302)
    
    def test_response_code_name(self):
        response = self.client.get(reverse('users:edit_profile'))
        self.assertEqual(response.status_code, 302)
    
    def test_redirect(self):
        response = self.client.get(reverse('users:edit_profile'))
        self.assertRedirects(response, '/users/login/?next=/users/profile/edit/')

