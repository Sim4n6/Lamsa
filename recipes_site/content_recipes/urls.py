from django.urls import path

from . import views

urlpatterns = [
    path("recipes/", views.home, name="home"),
    path("recipes/<int:recipe_id>/", views.detail, name="detail"),
]