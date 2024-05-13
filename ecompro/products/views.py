from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request,'index-2.html')


def product_list(request):

    product__list = Product.objects.all()
    context = {'products':product__list}
    return render(request,'product.html',context)




def viewproduct(request):
    return render(request,'singleproduct.html')
