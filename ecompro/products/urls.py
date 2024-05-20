from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('products',views.product_list,name="product"),
    
    path('view-product/<id>',views.viewproduct,name="viewproduct"),
]
