from django.urls import path
from library.views import AuthorListView


urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author-list'),
]