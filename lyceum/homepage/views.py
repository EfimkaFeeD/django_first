__all__ = ["home", "coffee"]

from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Item


def home(request):
    data = Item.objects.main_page()
    return render(request, "homepage/main.html", context={"items": data})


def coffee(request):
    return HttpResponse("Я чайник", status=418)
