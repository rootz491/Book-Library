from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.


def index(request):
    obj = Book.objects.all()[:3]
    context = {
        'books': obj,
    }
    return render(request, 'catalog/index.html', context)


def books(request):
    obj = Book.objects.all()
    context = {
        'books': obj,
    }
    return render(request, 'catalog/books.html', context)