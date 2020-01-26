from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("accueil/", views.home, name="home"),
    path("apropos/", views.home, name="about"),
    path("contact/", views.home, name="contact"),
    path("recipe/<int:recipe_id>/", views.detail_recette, name="detail"),
    path("travail_manuel/<int:travail_manuel_id>/", views.detail_travail_manuel, name="detail_travail_manuel"),
    path("admin/", views.admin, name="admin"),
] 