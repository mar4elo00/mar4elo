from contextlib import redirect_stderr
from apps import orders
from .models import *
from django.shortcuts import redirect, render

def Aorders(request):
    #pass
    if request.method == "GET":
        orders = Provider.objects.all()
        return render(request, "aorders.html")
    
    if request.method == "POST":
        company = request.POST.get("a")
        number= request.POST.get("b")
        mail = request.POST.get("c")
        face =  request.POST.get("d")
        
        Provider.objects.create(company=company,number=number,mail=mail, face=face)
        
        
        
        return redirect('orders')

def Acompanyordeers(request):
    #pass
    if request.method == "GET":
        companyordeers = CompanyOrdeers.objects.all()
        provider = Provider.objects.all()
        return render(request, "acompanyordeers.html", {"provider":provider})
    
    if request.method == "POST":
        uniqe_key = request.POST.get("a")
        name_product= request.POST.get("b")
        sumt = request.POST.get("c")
        units =  request.POST.get("d")
        providers=  request.POST.get("e")
        provider = Provider.objects.get(company=providers)
        status=  request.POST.get("f")
        CompanyOrdeers.objects.create(uniqe_key=uniqe_key,name_product=name_product,sumt=sumt, units=units, provider=provider,status=status )
        
        
        
        return redirect('companyordeers')