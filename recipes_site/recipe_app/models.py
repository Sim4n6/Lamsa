from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to="")
    pub_date = models.DateField("Date published")

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    ingredient =  models.TextField()

    def __str__(self):
        return self.ingredient

class Direction(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    direction =  models.TextField()

    def __str__(self):
        return self.direction