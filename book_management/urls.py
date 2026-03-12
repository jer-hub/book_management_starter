from django.urls import path
from . import views


app_name = "book_management"
urlpatterns = [
    path("", views.index, name="index"),
    path("book_create/", views.book_create, name="book_create"),
]