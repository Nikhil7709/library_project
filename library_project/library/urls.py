from django.urls import path
from library.views import AuthorListView, AuthorCreateView, BookListView, BookCreateView


urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/add/', AuthorCreateView.as_view(), name='author-add'),
    
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/add/', BookCreateView.as_view(), name='book-add'),
]