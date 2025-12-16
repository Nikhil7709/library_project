from django.shortcuts import render
from library.models import Author
from django.views import View

# Create your views here.

class AuthorListView(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'library/author_list.html', {'authors': authors})

