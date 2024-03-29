from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model,login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import *
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from .models import Utilisateur

# Create your views here.
def inscription(request):
    form = InscriptionForm()

    if request.method == "POST":
        # Create a mutable copy of the QueryDict
        mutable_request_data = request.POST.copy()
        
        if 'email' in mutable_request_data:
            mutable_request_data['username'] = mutable_request_data['email']

        form = InscriptionForm(mutable_request_data, request.FILES)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.lien_profile = f"https://smartcard.pythonanywhere.com/comptes/profile?id={user.id}"
            user.save()

            subject = "Création de compte"
            template = 'comptes/email.html'
            context = {'user':user}
            html_message = render_to_string(template, context)
            plain_message = strip_tags(html_message)  # Version texte brut du message
            recipient_list = ["dieuveilb840@gmail.com", "ridelntsoumou@gmail.com", "ngoukoulouemmanuelprecieux1@gmail.com"]
            try:
                send_mail(subject, plain_message, settings.EMAIL_HOST_USER, recipient_list, html_message=html_message) 
                return redirect('success')                           
            except:
                messages.error(request, "Un problème est survenu lors de l'envoi du mail, vérifiez votre connexion peut être")

    context = {'form': form}
    return render(request, 'comptes/inscription.html', context)



def success(request):
    
    return render(request, 'comptes/success.html')


def connexion(request):
    form = ConnexionForm()
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])       
            if user and not user.is_superuser:
                login(request, user)
                messages.success(request, f"Connexion réussie !!")
                return redirect('index')
            else:
                messages.error(request, f"Email et/ou Mot de passe incorrect !")

    context = {
        'form':form
    }

    return render(request, 'comptes/connexion.html', context)



def deconnexion(request):
    logout(request)
    messages.info(request, "Déconnexion réussie !")
    return redirect('index')



def profile(request):
    user = request.user
    try:
        if user.is_anonymous:
            id = request.GET.get("id")
        else:
            id = request.user.id
        user = Utilisateur.objects.get(id=id)

    except Exception as e:
        messages.error(request, f"Erreur : {e}")
        return redirect("index")
    context = {
        "user":user
    }
    return render(request, 'comptes/profile.html', context)


@login_required
def modifier_profile(request):
    if request.method == "POST":
        form = ModifierProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre profile a été modifié avec succès !")
            return redirect('index')
    else:
        form = ModifierProfileForm(instance=request.user)

    context = {
        'form':form
    }

    return render(request, "comptes/modifier_profile.html", context)