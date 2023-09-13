from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('Main:home')
            
        else:
            return render(request,"registration/login.html",{
                'error_message':"User or password are incorrect."
                })
    else:
        return render(request,'registration/login.html')
    
def logout_view(request):
    logout(request)
    messages.success(request,("Cerraste sesión!"))
    return redirect('Main:home')