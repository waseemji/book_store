from audioop import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import path,reverse
from .models import Book
from django.db.models import Avg

def index(request):
    books = Book.objects.all().order_by('rating')
    num_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))
    return render(request,"book_outlet/index.html",{
        "books":books,
        "total_number_of_books":num_books,
        "average_rating": avg_rating
    })

# Create your views here.

def book_details(request,slug):
    # try:
    #     books = Book.objects.get(pk=id)
    # except:
    #     raise Http404
    
    books = get_object_or_404(Book,slug=slug) 
    # redirect_to = reverse('book-detail',args=[books.slug])   
    return render(request,"book_outlet/book_details.html",{
        "title":books.title,
        "author":books.author,
        "rating":books.rating,
        "isbestseller":books.is_bestselling
    })

