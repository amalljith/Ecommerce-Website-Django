from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index-2.html')


def product(request):
    return render(request,'product.html')



def viewproduct(request):
    return render(request,'singleproduct.html')
