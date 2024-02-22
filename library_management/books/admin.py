from django.contrib import admin
from .models import Book, IssuedItem

# Register Book model with custom filters
class BookFilter(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ("book_name", "author_name", "quantity", "isbn", "description")
    
    # Filters to be displayed in the right sidebar
    list_filter = ("book_name", "author_name", "isbn", "description", "book_add_date")
    
    # Fields to be searched in the search bar
    search_fields = ("book_name", "author_name", "description")

# Register the Book model with the custom filters in the admin interface
admin.site.register(Book, BookFilter)

# Register IssuedItem model with custom filters
class IssuedItemFilter(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ("book_name", "username", "issue_date", "return_date")
    
    # Filters to be displayed in the right sidebar
    list_filter = ("issue_date", "return_date", "book_id__book_name", "user_id__username") 
    
    # Fields to be searched in the search bar
    search_fields = ("user_id__username", "book_id__book_name", "book_id__subject")

# Register the IssuedItem model with the custom filters in the admin interface
admin.site.register(IssuedItem, IssuedItemFilter)
