from catalog.models import Images, Item

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse


def item_list(request):
    template = loader.get_template("catalog/item_list.html")
    return HttpResponse(template.render({}, request))


def item_detail(request, item_id):
    template = loader.get_template("catalog/item.html")
    return HttpResponse(template.render({}, request))


def re_item_detail(request, re_item_id):
    return HttpResponse(re_item_id)


def item_converter(request, conv_item_id):
    return HttpResponse(conv_item_id)


def item_list(request):
    data = []
    for item in Item.objects.all():
        data.append(
            {
                "name": item.name,
                "path": reverse("catalog:item_detail", args=[item.id]),
                "category": item.category.name,
                "text": item.text,
                "main_image": item.main_image,
            }
        )
    return render(request, "catalog/item_list.html", context={"items": data})


def item_detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    images = Images.objects.filter(item=item_id).all()
    data = {
        "name": item.name,
        "category": item.category.name,
        "text": item.text,
        "main_image": item.main_image,
        "images": images,
    }
    return render(request, "catalog/item.html", context={"item": data})
