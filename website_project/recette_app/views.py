from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Recette, Travail_manuel, Activite

def index(request):
    return redirect("home")

def home(request):
    latest_recipes = Recette.objects.order_by('-pub_date')[:4]
    latest_travail_manuel = Travail_manuel.objects.order_by('-pub_date')[:4]
    latest_activite = Activite.objects.order_by('-pub_date')[:4]
    context = {'latest_recipes': latest_recipes, "latest_travail_manuel": latest_travail_manuel, "latest_activite":latest_activite}
    return render(request, 'recette_app/home.html', context)


def recipes(request):
    recipes = Recette.objects.order_by('-pub_date')
    context = {'recipes': recipes}
    return render(request, 'recette_app/recipes.html', context)

def activites(request):
    activites = Activite.objects.order_by('-pub_date')
    context = {'activites': activites}
    return render(request, 'recette_app/activites.html', context)

def travaux(request):
    travaux = Travail_manuel.objects.order_by('-pub_date')
    context = {'travaux': travaux}
    return render(request, 'recette_app/travaux.html', context)



def detail_recette(request, recipe_id):
    recipe = get_object_or_404(Recette, pk=recipe_id)
    ingredients = recipe.ingredients
    preparation = recipe.preparation
    context = {"recipe": recipe, "ingredients": ingredients, "preparation":preparation}
    return render(request, "recette_app/detail_recette.html", context)


def detail_travail_manuel(request, travail_manuel_id):
    travail_manuel = get_object_or_404(Travail_manuel, pk=travail_manuel_id)
    materiel = travail_manuel.materiel
    methode = travail_manuel.methode
    context = {"travail_manuel": travail_manuel, "materiel": materiel, "methode":methode}
    return render(request, "recette_app/detail_travail_manuel.html", context)

def detail_activite(request, activite_id):
    activite = get_object_or_404(Activite, pk=activite_id)
    context = {"activite": activite}
    return render(request, "recette_app/detail_activite.html", context)

def admin(request):
    return redirect("admin")