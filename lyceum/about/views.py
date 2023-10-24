__all__ = ["description"]

from django.http import HttpResponse
from django.template import loader


def description(request):
    template = loader.get_template("about/about.html")
    return HttpResponse(template.render({}, request))
