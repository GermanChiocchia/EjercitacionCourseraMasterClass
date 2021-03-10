from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Hello world</h1>')

def products(request):
    return HttpResponse('Products')
# Create your views here.
