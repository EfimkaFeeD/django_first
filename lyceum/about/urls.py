import about.views as views

from django.urls import path

urlpatterns = [path("", views.description, name="description")]
