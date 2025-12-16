from django.contrib import admin
from library.models import Author, Book

class BookInline(admin.TabularInline):
    """
    Allows managing books directly from the Author admin page
    """
    model = Book
    extra = 0
    fields = ['title', 'published_date']
    show_change_link = True


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'address']
    list_display_links = ['name', 'email']
    search_fields = ['name', 'email']
    list_filter = ['name']
    ordering = ['name']

    # Inline books
    inlines = [BookInline]
    save_as = True
    

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date']
    list_display_links = ['title']
    search_fields = ['title', 'author__name', 'author__email']
    list_filter = ['published_date', 'author']
    ordering = ['-published_date']
    save_as = True

    