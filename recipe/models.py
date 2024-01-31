from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# The recipe model
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    prep_time = models.PositiveIntegerField()  # in minutes
    cook_time = models.PositiveIntegerField()  # in minutes
    servings = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'
    
    def __str__(self):
        return self.title
