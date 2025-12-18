from django.shortcuts import redirect, render
from library.forms import AuthorForm, BookForm
from library.models import Author, Book
from django.views import View
from django.contrib import messages

# Create your views here.

class AuthorListView(View):
    def get(self, request):
        """
        Handles HTTP GET request.
        Fetches all Author records from the database
        and renders them in the author list template.
        """

        authors = Author.objects.all()
        return render(request, 'library/author_list.html', {'authors': authors})


# class AuthorCreateView(View):
#     def get(self, request):
#         """
#         Handles GET request.
#         Initializes an empty AuthorForm
#         and renders the author creation page.
#         """
#         form = AuthorForm()
        
#         # Render form template
#         return render(
#             request,
#             'library/author_form.html',
#             {'form': form}
#         )

#     def post(self, request):
#         """
#         Handles POST request.
#         Binds submitted data to the form,
#         validates it, and saves the record.
#         """
#         form = AuthorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('author-list')
        
#         # Re-render form with validation errors
#         return render(
#             request,
#             'library/author_form.html',
#             {'form': form}
#         )


class AuthorCreateView(View):
    # Template reused for both GET and POST responses
    template_name = 'library/author_form.html'

    def get(self, request):
        """
        Handles GET request.
        Displays an empty Author creation form.
        """
        form = AuthorForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """
        Handles POST request.
        Validates submitted form data
        and saves Author on success.
        """
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Author added successfully!")
            return redirect('author-list')
        else:
            # Form errors are automatically available in the template
            return render(
                request, 
                self.template_name, 
                {'form': form}
            )



class BookListView(View):
    """
    Handles GET request.
    Retrieves all books along with
    their related author data.
    """
    def get(self, request):
        # select_related optimizes DB queries for foreign key relationships
        books = Book.objects.select_related('author')
        
        # Render book list template with data
        return render(
            request,
            'library/book_list.html',
            {'books': books}
        )


"""
# This is just an example to illustrate the use of select_related
# Without select_related example:

books = Book.objects.all()
for book in books:
    book.author.name

"""



class BookCreateView(View):
    def get(self, request):
        """
        Handles GET request.
        Displays empty Book creation form.
        """
        form = BookForm()
        return render(
            request,'library/book_form.html',
            {'form': form}
        )

    def post(self, request):
        """
        Handles POST request.
        Validates submitted data
        and saves Book on success.
        """
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully!")
            return redirect('book-list')
        return render(
            request, 'library/book_form.html', 
            {'form': form}
        )


