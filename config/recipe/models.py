from django.db import models
from django.contrib.auth.models import User

# Model for categories
class Category(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='category_pictures/', blank=True, null=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
# Model for recipes
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipe_pictures/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'

    def __str__(self):
        return self.name
    
# Model for comments
class Comment(models.Model):
    comment = models.TextField(max_length=500)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.comment