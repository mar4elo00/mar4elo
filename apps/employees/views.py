from contextlib import redirect_stderr
from django.shortcuts import render

from apps import employees
from .models import *
from django.shortcuts import redirect, render

def Aindex(request):
    #pass
    if request.method == "GET":
        employees = Employee.objects.all()
        
        return render(request, "aindex.html", {"employees":employees})
    
    if request.method == "POST":
        first_name = request.POST.get("a")
        name = request.POST.get("b")
        surname = request.POST.get("c")
        date_of_birth = request.POST.get("d")
        email = request.POST.get("f")
        namber_of_phone =  request.POST.get("e")
        
        Employee.objects.create(first_name=first_name,name=name,surname=surname, date_of_birth=date_of_birth, email=email, namber_of_phone=namber_of_phone)
        
        
        
        return redirect('mark')
    
def Apassportdata(request):
    if request.method == "GET":
        employee= Employee.objects.all()
        return render(request, "apassportdata.html", {"employee":employee})
    
    if request.method == "POST":
        employeer= request.POST.get("employee")
        
        employee= Employee.objects.get(first_name=employeer)
       
        inn= request.POST.get("inn")
        no_passport= request.POST.get("nopassport")
        location=  request.POST.get("location")
        series=  request.POST.get("series")
        date_start= request.POST.get("datestart")
        date_end =  request.POST.get("dateend")
        Passport_Data.objects.create(employeer=employee,inn=inn, no_passport=no_passport,location=location, series=series,date_start=date_start,date_end=date_end)
        
        
        
        return redirect('passport')