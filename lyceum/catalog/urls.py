import catalog.views as views

from django.urls import path, re_path, register_converter


class PositiveIntConverter:
    regex = r"[1-9]\d*"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


register_converter(PositiveIntConverter, "posint")


urlpatterns = [
    path("", views.item_list, name="item_list"),
    path("<int:item_id>/", views.item_detail, name="item_detail"),
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
