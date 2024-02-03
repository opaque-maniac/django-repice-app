from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

# Model for the recipe itself
class Recipe(models.Model):
    BREAKFAST = 'Breakfast'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'
    DESSERT = 'Dessert'
    
    CATEGORY_CHOICES = [
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
        (DESSERT, 'Dessert'),
    ]

    author = models.ForeignKey(get_user_model(), related_name='recipes', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default=BREAKFAST)
    cover_image = models.ImageField(upload_to='recipe_images/', null=True, blank=True)
    description = models.CharField(max_length=500)
    content = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'
    
    def __str__(self):
        return self.title
