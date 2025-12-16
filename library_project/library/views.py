from django.shortcuts import redirect, render
from library.forms import AuthorForm, BookForm
from library.models import Author, Book
from django.views import View

# Create your views here.

class AuthorListView(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'library/author_list.html', {'authors': authors})


class AuthorCreateView(View):
    def get(self, request):
        form = AuthorForm()
        return render(request, 'library/author_form.html', {'form': form})

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author-list')
        return render(request, 'library/author_form.html', {'form': form})


class BookListView(View):
    def get(self, request):
        books = Book.objects.select_related('author')
        return render(request, 'library/book_list.html', {'books': books})


class BookCreateView(View):
    def get(self, request):
        form = BookForm()
        return render(
            request,'library/book_form.html',{'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
        return render(request, 'library/book_form.html', {'form': form})


