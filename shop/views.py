from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from math import ceil
# Create your views here.
def index(request):
    products = Products.objects.all()
    n = len(products)
    nslides = n//4 + ceil((n/4)+(n//4))
    params = {'no_of_slides':nslides,'range':range(nslides),'product':products}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse('We are at contact')

def tracker(request):
    return HttpResponse('We are at tracker')

def search(request):
    return HttpResponse('We are at search')

def prodview(request):
    return HttpResponse('We are at prodview')

def checkout(request):
    return HttpResponse('We are at checkout')


