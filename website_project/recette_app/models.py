from django.utils import timezone
from django.db import models

class Recette(models.Model):
    title = models.CharField("Titre", max_length=200)
    description = models.TextField("Description")
    photo = models.ImageField("Photo",upload_to="")
    ingredients =  models.TextField("Ingrédients")
    preparation =  models.TextField("Préparation")
    pub_date = models.DateField("Date published", default=timezone.now)

    def __str__(self):
        return self.title


class Travail_manuel(models.Model):
    title = models.CharField("Titre",max_length=200)
    description = models.TextField("Description")
    photo = models.ImageField("Photo", upload_to="")
    materiel =  models.TextField("Matériaux")
    methode =  models.TextField("Méthode")
    pub_date = models.DateField("Date published", default=timezone.now)

    def __str__(self):
        return self.title