from django.contrib import admin

# Register your models here.
from .models import Recipe, Ingredient, Direction

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Direction)