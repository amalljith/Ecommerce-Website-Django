from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request,'index-2.html')


def product_list(request):

    page = 1
    if request.GET:
        page=request.GET.get('page',1)

    product__list = Product.objects.all()
    product_paginator = Paginator(product__list,5)
    product__list = product_paginator.get_page(page)

    context = {'products':product__list}
    return render(request,'product.html',context)




def viewproduct(request):
    return render(request,'singleproduct.html')
