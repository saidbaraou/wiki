from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.entry_page, name="entry_page"),
    path("search/", views.search, name="search"),
    path("new-page/", views.new_page, name="new_page"),
    path("edit-content/", views.edit_content, name="edit_content")
]
