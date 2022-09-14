from tabnanny import verbose
from django.db import models



class Views_Product(models.Model):
    view = models.CharField(max_length=255, verbose_name="виды товара")
    
    class Meta:
        verbose_name="Вид товара"
        verbose_name_plural ="Вид товара"
   
    def __str__ (self):
        return self.view

class Appointment_Product(models.Model):
    appointment=models.CharField(max_length=255, verbose_name="назначение товара")
     
    class Meta:
        verbose_name = "назначение товара"
        verbose_name_plural = "назначение товара"
        
    def __str__(self):
        return self.appointment     
    
class Category (models.Model):
    appoinment=models.CharField(max_length=255, verbose_name="категории")
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"
    
    def __str__(self):
        return self.appoinment 
        

class Brend (models.Model):
    appointment=models.CharField(max_length=255, verbose_name="назначение бренда")
    face= models.CharField(max_length=30,verbose_name="Отвечающее лицо")
    contact=models.CharField(max_length=30,verbose_name="номер")
    email = models.EmailField()
    dogovor=models.CharField(max_length=255,verbose_name="Договор действителен до")
    status=models.CharField(max_length=255,verbose_name="статус сотруднечиства")

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренд"
        
    def __str__(self):
        return self.appointment
        
#товары
class Products(models.Model):
    name = models.CharField(max_length=255, verbose_name="наименование продукта")
    view = models.ForeignKey(to=Views_Product,on_delete=models.CASCADE, related_name="product", verbose_name="вид товара")
    appointment = models.ForeignKey(to=Appointment_Product,on_delete=models.CASCADE , verbose_name="Назначение")
    category= models.ForeignKey (to=Category,on_delete=models.CASCADE, verbose_name="Категория")
    brend= models.ForeignKey(to=Brend,on_delete=models.CASCADE , verbose_name="Бренд")
    sumt=models.IntegerField(verbose_name="количество товаров")
    scode=models.CharField(max_length=60,verbose_name="штрих код")
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товар"
        
    def __str__(self):
        return self.name + " --- " + self.category.appointment
        

class Haracteristic_Product(models.Model):
        product =models.ForeignKey(to=Products,on_delete=models.CASCADE, related_name="haracteristic_product", verbose_name="Товар")
        sostav = models.CharField(max_length=255,verbose_name="состав")
        color = models.CharField(max_length=255, verbose_name="цвет")
        
        class Meta:
            verbose_name = "Характеристика товара"
            verbose_name_plural = "Характеристика товара"
        
class Akcept (models.Model):
    acketp=models.CharField(max_length=255,verbose_name="Акцепт товаров")
    name = models.CharField(max_length=255, verbose_name="наименование продукта")
    view = models.ForeignKey(to=Views_Product,on_delete=models.CASCADE, related_name="akcept", verbose_name="Вид товара")
    appointment = models.ForeignKey(to=Appointment_Product,on_delete=models.CASCADE, verbose_name="Назначение")
    category= models.ForeignKey (to=Category,on_delete=models.CASCADE, verbose_name="Категория")
    brend= models.ForeignKey(to=Brend,on_delete=models.CASCADE, verbose_name="Бренд")
    sumt=models.IntegerField(verbose_name="количество товаров")
    daete=models.CharField(max_length=255,verbose_name="Дата продажи")
    scode=models.CharField(max_length=60,verbose_name="штрих код")
    
    class Meta:
        verbose_name = "проданный товар"
        verbose_name_plural = "проданный товар"
        
    def __str__(self):
        return self.name + " --- " + self.category.appointment
        
    
class Util (models.Model):
    name = models.CharField(max_length=255, verbose_name="наименование продукта")
    view = models.ForeignKey(to=Views_Product,on_delete=models.CASCADE, related_name="util", verbose_name="Вид товара")
    appointment = models.ForeignKey(to=Appointment_Product,on_delete=models.CASCADE, verbose_name="Назначение")
    category= models.ForeignKey (to=Category,on_delete=models.CASCADE, verbose_name="Категория")
    brend= models.ForeignKey(to=Brend,on_delete=models.CASCADE, verbose_name="Бренд")
    sumt=models.IntegerField(verbose_name="количество товаров")
    date=models.CharField(max_length=255,verbose_name="Дата списания")
    prichina=models.CharField(max_length=255,verbose_name="причина списания товара")
    scode=models.CharField(max_length=60,verbose_name="штрих код")
    
    class Meta:
        verbose_name = "списанный товар"
        verbose_name_plural = "списанный товар"
        
    def __str__(self):
        return self.name + " --- " + self.category.appointment
        
    
class Price (models.Model):
    product=models.ForeignKey(to=Products,on_delete=models.CASCADE, related_name="price",verbose_name="Товар")
    price=models.CharField(max_length=30,verbose_name="Цена")
    units=models.CharField(max_length=255,verbose_name="Единицы измерения")
    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цена"
        
class Accept (models.Model):
    name = models.CharField(max_length=255, verbose_name="наименование продукта")
    view = models.ForeignKey(to=Views_Product,on_delete=models.CASCADE, related_name="accept",verbose_name="Вид товара")
    appointment = models.ForeignKey(to=Appointment_Product,on_delete=models.CASCADE, verbose_name="Назначение")
    category= models.ForeignKey (to=Category,on_delete=models.CASCADE,verbose_name="Категория")
    brend= models.ForeignKey(to=Brend,on_delete=models.CASCADE,verbose_name="Бренд")
    sumt=models.IntegerField(verbose_name="количество товаров")
    scode=models.CharField(max_length=60,verbose_name="штрих код")
    date=models.DateField(max_length=255,verbose_name="дата приема")
    
    
    class Meta:
        verbose_name = "Принятый товар"
        verbose_name_plural = "Принятый товар"
        
    def __str__(self):
        return self.name + " --- " + self.category.appointment
        
