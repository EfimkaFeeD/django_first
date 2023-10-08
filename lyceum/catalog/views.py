from django.http import HttpResponse


def item_list(request):
    return HttpResponse("<body>Список элементов</body>")


def item_detail(request, item_id):
    return HttpResponse("<body>Подробно элемент</body>")


def re_item_detail(request, re_item_id):
    return HttpResponse(re_item_id)


def item_converter(request, conv_item_id):
    return HttpResponse(conv_item_id)
