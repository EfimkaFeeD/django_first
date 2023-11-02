__all__ = ["item_list", "item_detail", "re_item_detail", "item_converter"]

from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Item


def item_list(request):
    data = Item.objects.published()
    return render(request, "catalog/item_list.html", context={"items": data})


def item_detail(request, item_id):
    data = Item.objects.full_item_details(item_id)
    return render(request, "catalog/item.html", context={"item": data})


def re_item_detail(request, re_item_id):
    return HttpResponse(re_item_id)


def item_converter(request, conv_item_id):
    return HttpResponse(conv_item_id)
