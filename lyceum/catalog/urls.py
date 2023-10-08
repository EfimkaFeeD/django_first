from django.urls import path, re_path, register_converter

from . import views


class PositiveIntConverter:
    regex = r"[1-9]\d*"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


register_converter(PositiveIntConverter, "posint")


urlpatterns = [
    path("", views.item_list),
    path("<int:item_id>/", views.item_detail),
    re_path(r"^re/(?P<re_item_id>[1-9]\d*)/$", views.re_item_detail),
    path("converter/<posint:conv_item_id>/", views.item_converter),
]
