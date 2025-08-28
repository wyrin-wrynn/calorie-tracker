from django.urls import path

from . import views

urlpatterns = [
    path("health", views.healthz, name="healthz"),
    path("demo", views.demo, name="demo"),
    path("demo/ping", views.demo_ping, name="demo_ping"),
    path("aboutUs", views.aboutUs, name="aboutUs"),
]
