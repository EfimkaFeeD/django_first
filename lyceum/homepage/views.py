__all__ = ["home", "coffee"]

from django.http import Http404, HttpResponse
from django.shortcuts import render

from catalog.models import Item
from homepage.forms import EchoForm


def home(request):
    data = Item.objects.main_page()
    return render(request, "homepage/main.html", context={"items": data})


def coffee(request):
    return HttpResponse("Я чайник", status=418)


def echo(request):
    form = EchoForm(request.POST or None)
    return render(request, "homepage/echo.html", {"form": form})


def echo_submit(request):
    if request.method == "POST":
        return HttpResponse(request.POST["text"])
    raise Http404()
