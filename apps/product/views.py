from contextlib import redirect_stderr
from multiprocessing import context
from unicodedata import category, name
from apps import product
from .models import *
from django.shortcuts import redirect, render
from .forms import UploadFileForm

def product(request):
    #pass
    if request.method == "GET":
        product = Products.objects.all()
        view= Views_Product.objects.all()
        appointment= Appointment_Product.objects.all ()
        category=Category.objects.all ()
        brend= Brend.objects.all ()
        form = UploadFileForm(request.POST, request.FILES)
        context = {"product":product , "view":view,"appointment":appointment,"categoty":category,"brend":brend, "form":form}
        
        return render(request, "product.html",context)
    
    if request.method == "POST":
        name= request.POST.get("name")
        views= request.POST.get("view")
        view= Views_Product.objects.get(view=views)
        appointments= request.POST.get("appointment")
        appointment= Appointment_Product.objects.get(appointment=appointments)
        categorys=  request.POST.get("category")
        category= Category.objects.get(appoinment=categorys)
        brends=  request.POST.get("brend")
        brend= Brend.objects.get(appointment=brends)
        sumnt=  request.POST.get("sumnt")
        scode=  request.POST.get("scode")
        photo= request.FILES["file"]
        Products.objects.create(name=name,view=views,appointment=appointments, category=categorys, brend=appointment, sumnt=sumnt, scode=scode ,photo=photo)
        
def viewproduct(request):
    return render(request, "viewproduct.html" )

def ONOXOview(request):
        try:
            urna=Products.objects.all()
        
            return render(request, 'templates/viewproduct.html',{"urna":urna})
        except:
    
            urna = "Корзина пуста"
            return render (request, 'templates/viewproduct.html/',{"urna":urna})
   

