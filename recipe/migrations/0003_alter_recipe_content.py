# Generated by Django 4.2.7 on 2024-02-03 10:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_alter_recipe_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
