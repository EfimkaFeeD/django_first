from django.urls import path

import homepage.views as views

app_name = "homepage"

urlpatterns = [
    path("", views.home, name="home"),
    path("coffee/", views.coffee, name="coffee"),
]
