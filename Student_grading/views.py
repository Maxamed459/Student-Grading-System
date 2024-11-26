from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "grading/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "grading/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "grading/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return HttpResponseRedirect('register')

        if User.objects.filter(username=username).exists():
            messages= "Username already exists!"
            return HttpResponseRedirect('register', {
                "message":messages
            })

        # Create the user
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        return HttpResponseRedirect(reverse ('login'))

    return render(request, 'grading/register.html')