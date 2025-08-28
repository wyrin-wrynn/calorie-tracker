# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.timezone import now


def healthz(request):
    return JsonResponse("All ok!")


def demo(request):
    return render(request, "demo.html")


def demo_ping(request):
    ctx = {"ts": now()}
    return render(request, "partials/ping.html", ctx)


def aboutUs(request):
    return render(request, "aboutUs.html")
