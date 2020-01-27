from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("accueil/", views.home, name="home"),
    path("apropos/", views.home, name="about"),
    path("contact/", views.home, name="contact"),
    path("recipes/", views.recipes, name="recipes"),
    path("activites/", views.activites, name="activites"),
    path("travaux/", views.travaux, name="travaux"),
    path("recipe/<int:recipe_id>/", views.detail_recette, name="detail"),
    path("travail_manuel/<int:travail_manuel_id>/", views.detail_travail_manuel, name="detail_travail_manuel"),
    path("activite/<int:activite_id>/", views.detail_activite, name="detail_activite"),
    path("admin/", views.admin, name="admin"),
] 