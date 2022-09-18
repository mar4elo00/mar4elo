from contextlib import redirect_stderr
from itertools import product
from unicodedata import category
from xml.dom.minidom import Element
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from apps.product.models import Products
from .models import *
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

def register(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, 'register.html', {'form':form})
    if request.method == "POST":
        nickname =  request.POST.get("nickname")
        password = request.POST.get("password")
        name = request.POST.get("name")
        firstname = request.POST.get("firstname")
        email = request.POST.get("email")
        dob = request.POST.get("dob")
        User.objects.create_user(username=nickname, password=password, first_name=name, last_name=firstname, email = email)
        users = User.objects.latest("id")
        Register.objects.create(user = users, dob=dob)
        user = authenticate(username=nickname, password = password)
        login(request, user)
        return redirect("/")
            
            
def login_user(request):
    if request.method == "GET":
        return render(request, 'login.html',)
    
    if request.method == "POST":
        logins = request.POST.get("nickname")
        password = request.POST.get("password")
        user = authenticate(username=logins, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/")
            else:
                error = "Неверный логин или пароль"
                return render(request, 'login.html', {"error":error})
        else:
                error = "Неверный логин или пароль"
                return render(request, 'login.html', {"error":error})
            

def logout_user (request):
    logout(request)
    return redirect("/")

# @login_required
def urna(requset, id):
    if requset.method=="GET":
        urna= Urna.objects.filter(user_id=id)
        category = Category.objects.all()
        return render(requset,'urna.html',{"urna":urna, "category":category})