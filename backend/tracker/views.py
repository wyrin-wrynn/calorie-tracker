# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone


def healthz(request):
    return JsonResponse("All ok!")


def home(request):
    return render(request, "home.html")


def dashboard(request):
    return render(request, "dashboard.html")


def diary(request):
    meals = ["Breakfast", "Lunch", "Supper", "Dinner"]
    ctx = {
        "meals": meals,
        "today": timezone.localdate(),
    }
    return render(request, "diary.html", ctx)


def food_catalogue(request):
    return render(request, "food_catalogue.html")


def aboutUs(request):
    return render(request, "aboutUs.html")
