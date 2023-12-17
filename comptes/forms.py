from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class InscriptionForm(UserCreationForm):
    email1 = forms.EmailField(widget=forms.EmailInput(required=False))
    email2 = forms.EmailField(widget=forms.EmailInput(required=False))
    email3 = forms.EmailField(widget=forms.EmailInput(required=False))
    email4 = forms.EmailField(widget=forms.EmailInput(required=False))
    email5 = forms.EmailField(widget=forms.EmailInput(required=False))

    phone1 = forms.CharField(widget=forms.TextInput(required=False))
    phone2 = forms.CharField(widget=forms.TextInput(required=False))
    phone3 = forms.CharField(widget=forms.TextInput(required=False))
    phone4 = forms.CharField(widget=forms.TextInput(required=False))
    phone5 = forms.CharField(widget=forms.TextInput(required=False))

    fonction = forms.CharField(widget=forms.TextInput(required=False))
    siteweb = forms.URLField(widget=forms.URLInput(required=False))

    photo_couverture = forms.ImageField(widget=forms.FileInput(required=False))

    facebook = forms.URLField(widget=forms.URLInput(required=False))
    instagram = forms.URLField(widget=forms.URLInput(required=False))
    x = forms.URLField(widget=forms.URLInput(required=False))
    whatsapp_business = forms.URLField(required=False)
    quora = forms.URLField(widget=forms.URLInput(required=False))
    reddit = forms.URLField(widget=forms.URLInput(required=False))
    snapchat = forms.URLField(widget=forms.URLInput(required=False))
    pinterest = forms.URLField(widget=forms.URLInput(required=False))
    youtube = forms.URLField(widget=forms.URLInput(required=False))
    linkedin = forms.URLField(widget=forms.URLInput(required=False))
    medium = forms.URLField(widget=forms.URLInput(required=False))
    tiktok = forms.URLField(widget=forms.URLInput(required=False))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['email1', 'email2', 'email3', 'email4', 'email5',
				'phone1', 'phone2', 'phone3', 'phone4', 'phone5',
				'fonction', 'siteweb', 'photo_couverture',
				'facebook', 'instagram', 'x', 'whatsapp_business',
				'quora', 'reddit', 'snapchat', 'pinterest', 'youtube',
				'linkedin', 'medium', 'tiktok']


class ConnexionForm(forms.Form):
	username = forms.CharField(required=True,widget=forms.TextInput({'class':'form-control'}), label="Nom d'utilisateur")
	password = forms.CharField(widget=forms.PasswordInput({'class':'form-control'}), label="Mot de passe")
