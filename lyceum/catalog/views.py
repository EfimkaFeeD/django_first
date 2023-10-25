__all__ = ["item_list", "item_detail", "re_item_detail", "item_converter"]

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from catalog.models import Images, Item


def item_list(request):
    data = []
    for item in Item.objects.all():
        data.append(
            {
                "name": item.name,
                "path": reverse(
                    "catalog:item_detail_for_site",
                    args=[item.id],
                ),
                "category": item.category.name,
                "text": f"{item.text[:200]}...",
                "main_image": item.main_image,
            },
        )
    return render(request, "catalog/item_list.html", context={"items": data})


def item_detail(request, item_id):
    return HttpResponse("<body>Подробно элемент</body>")


def item_detail_for_site(request, item_id_for_site):
    item = Item.objects.get(pk=item_id_for_site)
    images = Images.objects.filter(item=item_id_for_site).all()
    data = {
        "name": item.name,
        "category": item.category.name,
        "text": item.text,
        "main_image": item.main_image,
        "images": images,
    }
    return render(request, "catalog/item.html", context={"item": data})


def re_item_detail(request, re_item_id):
    return HttpResponse(re_item_id)


def item_converter(request, conv_item_id):
    return HttpResponse(conv_item_id)
