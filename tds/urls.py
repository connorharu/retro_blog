from django.urls import path

from . import views

urlpatterns = [
    path("3ds/", views.tds_main, name="3ds"),
]