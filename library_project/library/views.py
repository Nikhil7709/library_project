from django.shortcuts import render
from library.models import Author
# Create your views here.

class AuthorListView:
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'library/author_list.html', {'authors': authors})

