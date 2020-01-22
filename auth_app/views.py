from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout, get_user_model
# Create your views here.

def auth(request):
    return render(request, 'auth.html')

def login(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        user = authenticate(request, email=email, password=password)
        print(user)
    return redirect('auth')


def signup(request):
    if request.POST:
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = data['password']
        print(request.POST)
        if get_user_model().objects.create_user(f"{first_name} {last_name}", email, password) is not None:
            return redirect('/')
    return redirect('auth')

def logout(request):
    logout(request)
    return redirect('/auth')
