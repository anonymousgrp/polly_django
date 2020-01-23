from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout, get_user_model


def auth(request):
    return render(request, 'auth.html')


def login_handler(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return redirect('auth')


def signup(request):
    if request.POST:
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = data['password']
        user = get_user_model().objects.create_user(
            f"{first_name}", email, password)
        if user is not None:
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect('/')
    return redirect('auth')


def logout_handler(request):
    logout(request)
    return redirect('auth')
