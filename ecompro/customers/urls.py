from django.urls import path

from . import views

urlpatterns = [
    
    path('login',views.show_account,name="account"),
    path('logout',views.logoutt,name="logout"),
    
]
