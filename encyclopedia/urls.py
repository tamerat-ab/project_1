from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("create_page", views.create_page, name="create_page"),
    path("save_page", views.save_page, name="save_page"),
    path("edit_page/<str:title>", views.edit_page, name="edit_page"),
    path("save_change", views.save_change, name="save_change"),
    path("random_page", views.random_page, name="random_page"),
]
