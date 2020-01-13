from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField( )
    pub_date = models.DateField("Date published")

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    ingredient =  models.CharField(max_length=200)
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient

class Direction(models.Model):
    direction =  models.CharField(max_length=200)
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)

    def __str__(self):
        return self.direction