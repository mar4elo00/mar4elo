from __future__ import division
from ast import Try

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


def ONOXOview(request):
    return render(request,"home/index.html")


