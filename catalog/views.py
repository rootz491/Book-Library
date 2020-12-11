from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Book, BookInstance
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


'''     basic generic class view

class SomeView(generic.DetailView):
    model = Book
    context_object_name = 'books'   # context variable name
    template_name = 'catalog/details.html'  # custom template name  (default: 'model_detail.html')
    queryset = Book.objects.filter(author='abc')    # customise content variable

    # another way to modify data before sending.  (can do the same with queryset variable as above)
    def get_queryset(self):
        return Book.objects

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
'''




class IndexView(LoginRequiredMixin, generic.ListView,):
    login_url = 'login'
    model = Book
    template_name = 'catalog/index.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()[:3]





class BookListView(LoginRequiredMixin, generic.ListView):
    login_url = 'login'
    model = Book
    template_name = 'catalog/books.html'
    context_object_name = 'books'



class BookDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = 'login'
    model = Book
    template_name = 'catalog/detail_book.html'










