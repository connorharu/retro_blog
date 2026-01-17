from django.urls import path

from . import views

urlpatterns = [
    path("wii/", views.wii_main, name="wii"),
]