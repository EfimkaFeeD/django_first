from django.http import HttpResponse
from django.template import loader


def home(request):
    template = loader.get_template("homepage/main.html")
    return HttpResponse(template.render({}, request))


def coffee(request):
    return HttpResponse("Я чайник", status=418)
