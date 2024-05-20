from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    products = Product.objects.all()
    context= {"pro":products}
    return render(request,'index-2.html',context)


def product_list(request):

    page = 1
    if request.GET:
        page=request.GET.get('page',1)

    product__list = Product.objects.order_by('-priority')
    product_paginator = Paginator(product__list,2)
    product__list = product_paginator.get_page(page)

    context = {'products':product__list}
    return render(request,'product.html',context)




def viewproduct(request,id):
    product_list = Product.objects.get(id=id)
    context = {'product':product_list}
    return render(request,'singleproduct.html',context)
