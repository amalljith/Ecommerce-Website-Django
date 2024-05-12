from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('products',views.product,name="product"),
    
    path('view-product',views.viewproduct,name="viewproduct"),
]
