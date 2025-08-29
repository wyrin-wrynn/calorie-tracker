from django.urls import path

from . import views

urlpatterns = [
    path("health", views.healthz, name="healthz"),
    path("", views.home, name="home"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("diary", views.diary, name="diary"),
    path("food_catalogue", views.food_catalogue, name="food_catalogue"),
    path("aboutUs", views.aboutUs, name="aboutUs"),
]
