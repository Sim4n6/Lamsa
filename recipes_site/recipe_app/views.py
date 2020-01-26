from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Recette, Travail_manuel

def index(request):
    return redirect("home")

def home(request):
    latest_recipes = Recette.objects.order_by('-pub_date')[:4]
    context = {'latest_recipes': latest_recipes}
    return render(request, 'recipe_app/home.html', context)


def detail(request, recipe_id):
    recipe = get_object_or_404(Recette, pk=recipe_id)
    ingredients = recipe.ingredients
    preparation = recipe.preparation
    latest_recipes = Recette.objects.order_by('-pub_date')[:4]
    context = {"recipe": recipe, "ingredients": ingredients, "preparation":preparation,"latest_recipes": latest_recipes}
    return render(request, "recipe_app/detail.html", context)


def admin(request):
    return redirect("admin")