# Generated by Django 3.0.2 on 2020-01-19 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recette_app', '0004_recipe_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(default="", upload_to='recipe_photos'),
            preserve_default=False,
        ),
    ]
