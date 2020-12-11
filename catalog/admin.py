from django.contrib import admin
from .models import *

# Register your models here.


# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Language)
# admin.site.register(Genre)
# admin.site.register(Author)


# to show other data while listing objects from database in admin panel.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]        # to organise the way of input fields, it's alignments (vertical or horizontal) etc.


# admin.site.register(Author, AuthorAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    # inlines = ['BooksInstanceInline']


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'id', 'status', 'due_back', 'borrower')     # display this data in unique columns
    list_filter = ('status', 'due_back')                    # to add filter on the right-side of book

    fieldsets = (           # to group certain fields under specific heading in input form.
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

