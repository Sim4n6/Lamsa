from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=600)
    pub_date = models.DateField('Date published')

    def __str__(self):
        return self.title