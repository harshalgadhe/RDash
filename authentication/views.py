from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.

def homepage(request):
    if request.user.is_authenticated == True:
        return redirect('/tasks')
    return render(request, "homepage.html")

def login_user(request):
    if request.user.is_authenticated == True:
        return redirect('/tasks')
    return render(request, "login.html")

def signup_user(request):
    if request.user.is_authenticated == True:
        return redirect('/tasks')
    return render(request, "signup.html")

def create_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(request.POST)
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User Already Exists')
            return redirect('/')

        User.objects.create_user(
            username = username,
            email = email,
            password = password
        )
        messages.success(request, 'Successfully Created User. Please Log In')
    return redirect('/')

def authenticate_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Successful")
            return redirect('/tasks')
        else:
            messages.error(request, "Incorrect Credentials Given")
            return redirect('/login')
    return redirect('/')

def logout_user(request):
    messages.success(request, "Logged Out Successfully")
    logout(request)
    return redirect('/')