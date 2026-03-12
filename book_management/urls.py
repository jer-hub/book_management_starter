from django.urls import path
from . import views


app_name = "book_management"
urlpatterns = [
    path("", views.index, name="index")
]