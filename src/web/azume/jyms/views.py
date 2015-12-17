from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Jym


def home_page(request):
    return render(request, "home.html", {"jyms": Jym.objects.all()})

def add_jym(request):
    number = Jym.objects.count() + 1

    jym = Jym()
    jym.lat = request.POST["lat"]
    jym.lng = request.POST["lng"]
    jym.name = "Guy #{0}".format(number)
    jym.save()

    return HttpResponse()
