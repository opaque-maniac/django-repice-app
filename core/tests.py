from django.test import TestCase
from django.urls import reverse

# Tests for the core app

# Test for the home page view
class TestHomePageView(TestCase):
    def test_response_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_response_code_name(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_used(self):
        response = self.client.get(reverse('core:home'))
        self.assertTemplateUsed(response, 'core/home.html')

# Test for the about page view
class TestAboutPageView(TestCase):
    def test_response_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    
    def test_response_code_name(self):
        response = self.client.get(reverse('core:about'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_used(self):
        response = self.client.get(reverse('core:about'))
        self.assertTemplateUsed(response, 'core/about.html')

# Test for the contact page view
class TestContactPageView(TestCase):
    def test_response_code(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
    
    def test_response_code_name(self):
        response = self.client.get(reverse('core:contact'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_used(self):
        response = self.client.get(reverse('core:contact'))
        self.assertTemplateUsed(response, 'core/contact.html')

# Test for the terms page view
class TestTermsPageView(TestCase):
    def test_response_code(self):
        response = self.client.get('/terms/')
        self.assertEqual(response.status_code, 200)
    
    def test_response_code_name(self):
        response = self.client.get(reverse('core:terms'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_used(self):
        response = self.client.get(reverse('core:terms'))
        self.assertTemplateUsed(response, 'core/terms.html')
