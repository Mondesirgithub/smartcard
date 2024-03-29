from django.urls import path
from django.contrib.auth import views
from . import views as myviews


urlpatterns = [
    path('inscription/', myviews.inscription, name='inscription'),
    path('modification_profile/', myviews.modifier_profile, name='modifier_profile'),
    path('success/', myviews.success, name='success'),
    path('connexion/', myviews.connexion, name='connexion'),
    path('profile/', myviews.profile, name='profile'),
    path('deconnexion/', myviews.deconnexion, name='deconnexion'),
    path('reset_password/', views.PasswordResetView.as_view(template_name="comptes/password_reset.html"), name='password_reset'),
    path('reset_password_sent/', views.PasswordResetDoneView.as_view(template_name="comptes/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(template_name="comptes/password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', views.PasswordResetCompleteView.as_view(template_name="comptes/password_reset_done.html"), name='password_reset_complete'),
]