from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from math import ceil
# Create your views here.
def index(request):
    # products= Products.objects.all()
    

    allProds = []
    catprods = Products.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Products.objects.filter(category=cat)
        n= len(prod)
        nSlides= n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    # allProds=[[products, range(1, len(products)), nSlides],[products, range(1, len(products)), nSlides]]
    params={'allProds':allProds }
    return render(request,"shop/index.html", params)


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


