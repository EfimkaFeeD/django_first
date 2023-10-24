from django.urls import path

import about.views as views


app_name = "about"

urlpatterns = [path("", views.description, name="description")]
