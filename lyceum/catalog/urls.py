__all__ = ["PositiveIntConverter"]

from converters.posint import PositiveIntConverter
from django.urls import path, re_path, register_converter

import catalog.views as views


app_name = "catalog"

register_converter(PositiveIntConverter, "posint")


urlpatterns = [
    path("", views.item_list, name="item_list"),
    path("<int:item_id>/", views.item_detail, name="item_detail"),
    path(
        "item/<int:item_id_for_site>/",
        views.item_detail_for_site,
        name="item_detail_for_site",
    ),
    re_path(
        r"^re/(?P<re_item_id>[1-9]\d*)/$",
        views.re_item_detail,
        name="re_item_detail",
    ),
    path(
        "converter/<posint:conv_item_id>/",
        views.item_converter,
        name="item_converter",
    ),
]
