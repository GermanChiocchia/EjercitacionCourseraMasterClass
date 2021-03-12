from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Book

def index(request):
    book_list = Book.objects.all()
    context = {
        'book_list':book_list
    }
    return render(request,'myapp/index.html', context)

def detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'myapp/detail.html',{'book':book})

def add_book(request):
    if request.method == "POST":
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        price = request.POST.get('price',)
        book_image = request.FILES['book_image']

        book = Book(name=name, desc=desc, price=price, book_image=book_image)
        book.save()
        
    return render(request, 'myapp/add_book.html')
# Create your views here.
