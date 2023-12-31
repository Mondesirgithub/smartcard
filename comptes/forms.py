from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class InscriptionForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput, required=False)
    adresse = forms.CharField(widget=forms.TextInput, required=True, error_messages={'required': 'L\'adresse est obligatoire'})
    first_name = forms.CharField(widget=forms.TextInput, required=True, error_messages={'required': 'Le prénom est obligatoire'})
    last_name = forms.CharField(widget=forms.TextInput, required=True, error_messages={'required': 'Le nom est obligatoire'})
    
    
    email = forms.EmailField(widget=forms.EmailInput, required=False)
    email1 = forms.EmailField(widget=forms.EmailInput, required=True, error_messages={'required': 'Le premier email est obligatoire'})
    phone1 = forms.CharField(widget=forms.TextInput, required=True, error_messages={'required': 'Le premier numéro de téléphone est obligatoire'})
    fonction = forms.CharField(widget=forms.TextInput, required=True, error_messages={'required': 'La fonction est obligatoire'})
    photo_couverture = forms.ImageField(widget=forms.FileInput, required=False)
    photo_profile = forms.ImageField(widget=forms.FileInput, required=True, error_messages={'required': 'La photo de profile est obligatoire'})
    
    email2 = forms.EmailField(widget=forms.EmailInput, required=False)
    email3 = forms.EmailField(widget=forms.EmailInput, required=False)
    email4 = forms.EmailField(widget=forms.EmailInput, required=False)
    email5 = forms.EmailField(widget=forms.EmailInput, required=False)

    
    phone2 = forms.CharField(widget=forms.TextInput, required=False)
    phone3 = forms.CharField(widget=forms.TextInput, required=False)
    phone4 = forms.CharField(widget=forms.TextInput, required=False)
    phone5 = forms.CharField(widget=forms.TextInput, required=False)

    siteweb = forms.URLField(widget=forms.URLInput, required=False)

    facebook = forms.URLField(widget=forms.URLInput, required=False)
    instagram = forms.URLField(widget=forms.URLInput, required=False)
    x = forms.URLField(widget=forms.URLInput, required=False)
    whatsapp_business = forms.URLField(widget=forms.URLInput, required=False)
    quora = forms.URLField(widget=forms.URLInput, required=False)
    reddit = forms.URLField(widget=forms.URLInput, required=False)
    snapchat = forms.URLField(widget=forms.URLInput, required=False)
    pinterest = forms.URLField(widget=forms.URLInput, required=False)
    youtube = forms.URLField(widget=forms.URLInput, required=False)
    linkedin = forms.URLField(widget=forms.URLInput, required=False)
    medium = forms.URLField(widget=forms.URLInput, required=False)
    tiktok = forms.URLField(widget=forms.URLInput, required=False)


    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'adresse', 'first_name', 'last_name', 'email','email1', 'phone1', 'fonction',
                  'photo_couverture','photo_profile', 'email2', 'email3', 'email4', 'email5', 'phone2', 'phone3', 'phone4',
                  'phone5', 'siteweb', 'facebook', 'instagram', 'x', 'whatsapp_business', 'quora', 'reddit',
                  'snapchat', 'pinterest', 'youtube', 'linkedin', 'medium', 'tiktok']


class ConnexionForm(forms.Form):
	username = forms.CharField(required=True,widget=forms.TextInput({'placeholder':'adresse email'}), label="")
	password = forms.CharField(required=True, widget=forms.PasswordInput({'placeholder':'mot de passe'}), label="")
