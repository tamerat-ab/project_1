from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("create_page", views.create_page, name="create_page"),
    path("save_page", views.save_page, name="save_page"),
]
