from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sfc/", views.sfc_main, name="sfc"),
]