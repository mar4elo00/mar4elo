from __future__ import division
from ast import Try
from itertools import product

from django.db.models import Q
from django.http import BadHeaderError, HttpResponse
from django.views.generic import ListView,DetailView
from django.shortcuts import redirect, render
from .models import *
from django.views.generic.base import View
from .forms import *
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import datetime 
from email.mime.text import MIMEText
import smtplib
from random import randint
from datetime import date

from django.contrib.auth.decorators import login_required, user_passes_test
from apps.product.models import *
from apps.users.models import Urna

def ONOXOview(request):
    if request.method == "GET":
        try:
            urna=Products.objects.all()
            category = Category.objects.all()
            categorys = None
            return render(request, 'home/index.html',{"urna":urna, "category":category, "categorys":categorys})
        except:
            category = Category.objects.all()
            urna = "Корзина пуста"
            categorys = None
            return render (request, 'home/index.html/',{"urna":urna,"category":category, "categorys":categorys})
   
    if request.method == "POST":
        urna=Products.objects.all()
        category = Category.objects.all()
        categorys = request.POST.get("categorys")
        
        
        userid = request.POST.get("userid")
        if userid != None:
            user = User.objects.get(id=userid)
            product = request.POST.get("product")
            name_product = Products.objects.get(id=product)
            summ = request.POST.get("summ")
            Urna.objects.create(user=user, name_product=name_product , summ=summ)
        return render (request, 'home/index.html/',{"urna":urna,"category":category, "categorys":categorys})

