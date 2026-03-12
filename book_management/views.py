from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    return render(request, "book_management/index.html", {
        "books": Book.objects.all(),
    })
