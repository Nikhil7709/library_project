from django.urls import path
from library.views import AuthorListView, AuthorCreateView


urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/add/', AuthorCreateView.as_view(), name='author-add'),
]