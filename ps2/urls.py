from django.urls import path

from . import views

urlpatterns = [
    path("ps2/", views.ps2_main, name="ps2"),
]