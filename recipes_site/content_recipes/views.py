from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recipe, Ingredient, Direction


def home(request):
    latest_recipes = Recipe.objects.order_by('-pub_date')[:4]
    context = {'latest_recipes': latest_recipes}
    return render(request, 'content_recipes/home.html', context)


def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    ingredients = Ingredient.objects.filter(recipe__id=recipe_id)
    directions = Direction.objects.filter(recipe__id=recipe_id)
    return render(request, "content_recipes/detail.html", {"recipe": recipe, "ingredients": ingredients, "directions": directions})