from django.urls import path

from . import views

urlpatterns = [
    path("registrar/", views.cadastro_supervisor, name="registrar"),
    path("login/", views.login_supervisor, name="login_supervisor"),
    path("logout/", views.logout_supervisor, name="logout_supervisor"),
]