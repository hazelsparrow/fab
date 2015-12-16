from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


def home_page(request):
    return render(request, "home.html")

def add_jym(request):
    return HttpResponse()
