from django.db import models

class Recette(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to="")
    ingredients =  models.TextField()
    preparation =  models.TextField()
    pub_date = models.DateField("Date published")

    def __str__(self):
        return self.title


class Travail_manuel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to="")
    materiel =  models.TextField()
    methode =  models.TextField()
    pub_date = models.DateField("Date published")

    def __str__(self):
        return self.title