from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('pricing-plan/', views.pricing_plan, name='pricing_plan'),
]
