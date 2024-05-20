from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Customer
from django.contrib import messages  

# Create your views here.
def show_account(request):
    if request.POST and 'register' in request.POST:
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')

            if password1==password2:
            
             if User.objects.filter(email=email).exists():
                 messages.info(request,('email taken'))
                 return redirect('account')
             else:
             #creates user accounts

                user=User.objects.create_user(
                    username=username,
                    password=password1,
                    email=email
                )
                messages.info(request,('successfully registered'))
            
            else:
             messages.info(request,('password not match'))
             return redirect('account')    
            #creates customer accounts
            Customer.objects.create(
                user=user

            )
            return redirect('index')
        except Exception as e:
         error_message="duplicate usernaame or invalid inputs"
         messages.error (request,error_message)

    if request.POST and 'login' in request.POST:
       username=request.POST.get('username')
       password=request.POST.get('password')
       user=authenticate(username=username,password=password)
       if user:
          login(request,user)
          return redirect('index')
       else:
          messages.error(request,'invalid user credentials')
    
    return render(request,'account.html')


def logoutt(request):
   logout(request)
   return redirect('index')