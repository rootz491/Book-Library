from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from .models import Book, BookInstance
from .forms import RenewBookForm
import datetime


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


class LoanedBookByUser(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renewBook(request, pk):
    book = get_object_or_404(BookInstance, pk=pk)

    if request.method == 'POST':
        form = RenewBookForm(request.POST)

        if form.is_valid():
            book.due_back = form.cleaned_data['renewal_date']
            book.save()

            return redirect('catalog:borrowed')

    else:
        # default renewal date
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book,
    }

    return render(request, 'catalog/book_renew.html', context)


class BookUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Book
    login_url = 'login'
    permission_required = ('can_edit_book',)
    fields = '__all__'



