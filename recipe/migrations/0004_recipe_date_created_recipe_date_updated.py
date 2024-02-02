# Generated by Django 4.2.7 on 2024-02-01 21:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_remove_ingredient_recipe_remove_instruction_recipe_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]