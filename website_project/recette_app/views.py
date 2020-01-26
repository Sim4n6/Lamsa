from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Recette, Travail_manuel

def index(request):
    return redirect("home")

def home(request):
    latest_recipes = Recette.objects.order_by('-pub_date')[:4]
    latest_travail_manuel = Travail_manuel.objects.order_by('-pub_date')[:4]
    context = {'latest_recipes': latest_recipes, "latest_travail_manuel": latest_travail_manuel}
    return render(request, 'recette_app/home.html', context)


def detail_recette(request, recipe_id):
    recipe = get_object_or_404(Recette, pk=recipe_id)
    ingredients = recipe.ingredients
    preparation = recipe.preparation
    latest_recipes = Recette.objects.order_by('-pub_date')[:4]
    context = {"recipe": recipe, "ingredients": ingredients, "preparation":preparation,"latest_recipes": latest_recipes}
    return render(request, "recette_app/detail_recette.html", context)


def detail_travail_manuel(request, travail_manuel_id):
    travail_manuel = get_object_or_404(Travail_manuel, pk=travail_manuel_id)
    materiel = travail_manuel.materiel
    methode = travail_manuel.methode
    latest_travail_manuel = Travail_manuel.objects.order_by('-pub_date')[:4]
    context = {"travail_manuel": travail_manuel, "materiel": materiel, "methode":methode,"latest_travail_manuel": latest_travail_manuel}
    return render(request, "recette_app/detail_travail_manuel.html", context)

def admin(request):
    return redirect("admin")