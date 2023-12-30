from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils.functions import *
import os
# Create your models here.


def user_cover_photo_path(instance, filename):
    user_folder = f"{instance.last_name}_{instance.first_name}"
    today = datetime.today()
    date_folder = today.strftime("%Y/%m/%d")
    filename = f"{today.strftime('%H-%M-%S')}_{filename}"
    return os.path.join('photos_couv', user_folder, date_folder, filename)


def user_profile_photo_path(instance, filename):
    user_folder = f"{instance.last_name}_{instance.first_name}"
    today = datetime.today()
    date_folder = today.strftime("%Y/%m/%d")
    filename = f"{today.strftime('%H-%M-%S')}_{filename}"
    return os.path.join('photos_profile', user_folder, date_folder, filename)

class Utilisateur(AbstractUser):
    adresse = models.CharField(max_length=255, blank=False)
    email1 = models.EmailField(blank=False)
    email2 = models.EmailField(blank=True)
    email3 = models.EmailField(blank=True)
    email4 = models.EmailField(blank=True)
    email5 = models.EmailField(blank=True)

    phone1 = models.CharField(max_length=15, blank=False)
    phone2 = models.CharField(max_length=15, blank=True)
    phone3 = models.CharField(max_length=15, blank=True)
    phone4 = models.CharField(max_length=15, blank=True)
    phone5 = models.CharField(max_length=15, blank=True)

    fonction = models.CharField(max_length=255, blank=False)
    siteweb = models.URLField(blank=True)

    photo_couverture = models.ImageField(upload_to=user_cover_photo_path, blank=True, null=True)
    photo_profile = models.ImageField(upload_to=user_profile_photo_path, blank=False, null=False)

    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    x = models.URLField(blank=True)
    whatsapp_business = models.URLField(blank=True)
    quora = models.URLField(blank=True)
    reddit = models.URLField(blank=True)
    snapchat = models.URLField(blank=True)
    pinterest = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    medium = models.URLField(blank=True)
    tiktok = models.URLField(blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} - {self.email}"
    