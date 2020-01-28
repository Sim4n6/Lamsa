from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

from .models import Recette, Travail_manuel, Activite

def index(request):
    return redirect("home")

def apropos(request):
    return render(request, 'recette_app/apropos.html')

def contact(request):
    return render(request, 'recette_app/contact.html')

def reponse(request):
    message_old = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    
    # send_mail(
    #     '[From LAMSA website]',
    #     f'{ message }',
    #     f'{ from_email }',
    #     ['sim4n6@gmail.com'],
    # fail_silently=False,
    # )    

    message = Mail(
        from_email=from_email,
        to_emails='giqeppappah-7503@yopmail.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print("--->", str(e))

    return render(request, 'recette_app/reponse.html')

def home(request):
    latest_recipes = Recette.objects.order_by('-pub_date')[:3]
    latest_travail_manuel = Travail_manuel.objects.order_by('-pub_date')[:3]
    latest_activite = Activite.objects.order_by('-pub_date')[:3]
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