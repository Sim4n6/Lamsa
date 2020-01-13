from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField(verbose_name="Ingredients", default="Ingredients ... ")
    directions = models.TextField(verbose_name="Directions", default="Directions ... ")
    pub_date = models.DateField("Date published")

    def __str__(self):
        return self.title