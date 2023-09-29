from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User

def homepage(request):
    """
    Renders the home page consisting of login and signup button
    @params: Http Request
    returns: Http Response
    """
    #checking if user is already authenticated
    if request.user.is_authenticated == True:
        return redirect('/tasks')
    return render(request, "homepage.html")

def login_user(request):
    """
    Renders the login page
    @params: Http Request
    returns: Http Response
    """
    #checking if user is already authenticated
    if request.user.is_authenticated == True:
        return redirect('/tasks')
    return render(request, "login.html")

def signup_user(request):
    """
    Renders the signup
    @params: Http Request
    returns: Http Response
    """
    #checking if user is already authenticated
    if request.user.is_authenticated == True:
        return redirect('/tasks')
    return render(request, "signup.html")

def create_user(request):
    """
    Creates new user if no such user exists
    @params: Http Request
    returns: Http Response
    """
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        #checking if the given username already exists in db
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
    """
    Authenticate the user against given credentials
    @params: Http Request
    returns: Http Response
    """
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
    """
    Function used for logging out, by deleting the session cookie
    @params: Http Request
    returns: Http Response
    """
    messages.success(request, "Logged Out Successfully")
    logout(request)
    return redirect('/')