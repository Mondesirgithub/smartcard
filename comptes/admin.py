from django.contrib import admin
from .models import Utilisateur

class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('username','last_name', 'first_name','fonction', 'siteweb')
    search_fields = ('last_name', 'first_name', 'email', 'fonction')
    list_filter = ('fonction',)
    fieldsets = (
        ('Informations personnelles', {'fields': ('last_name', 'first_name', 'adresse', 'photo_couverture', 'photo_profile', 'email1','email2','email3','email4','email5')}),
        ('Informations professionnelles', {'fields': ('fonction', 'facebook', 'instagram', 'whatsapp_business', 'quora', 'reddit', 'snapchat', 'pinterest', 'youtube', 'linkedin', 'medium', 'tiktok', 'siteweb', 'lien_profile')}),
        ('informations de connexion', {'fields': ('username', 'email', 'password', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'is_staff', 'is_active', 'date_joined')}),
    )


    def get_fields(self, request, obj=None):
        # Récupérer tous les champs du modèle
        fields = [field.name for field in Utilisateur._meta.get_fields()]
        return fields

admin.site.register(Utilisateur, UtilisateurAdmin)

admin.site.site_title = "SMART CARD"
admin.site.site_header = "ADMINISTRATION SMART CARD"
admin.site.index_title = "Site d'administration"
