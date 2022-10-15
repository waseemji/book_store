from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    prepopulated_fields= {"slug":("title",)}
    list_filter = ("rating","author")

admin.site.register(Book,BookAdmin)
