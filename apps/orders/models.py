from unittest.util import _MAX_LENGTH
from django.db import models

class Provider (models.Model):
    company=models.CharField(max_length=255,verbose_name="компания поставщика")
    number=models.CharField(max_length=30,verbose_name="номер поставщика")
    mail=models.EmailField()
    face=models.CharField(max_length=255,verbose_name="ответсвенное лицо")
    
    class Meta:
        verbose_name="поставщика"
        verbose_name_plural="поставщик"
#@property
#    def provider_information (self):
#       return self.company + " - " + self.number + " - " + self.mail + " - " + self.face
         
    def __str__(self):
        return self.company


class CompanyOrdeers (models.Model):
    uniqe_key=models.CharField(max_length=255,verbose_name="уникальный ключ")
    name_product=models.CharField(max_length=255,verbose_name="Наименование товара")
    sumt=models.IntegerField(verbose_name="количество")
    units=models.CharField(max_length=255,verbose_name="единицы измерения")
    provider=models.ForeignKey(to=Provider, on_delete=models.CASCADE, related_name="companyordeers", verbose_name="Поставщик")
    status=models.CharField(max_length=255,verbose_name="статус заказа", blank=True, null=True)
    
    class Meta :
        verbose_name="Заказы для компании"
        verbose_name_plural="Заказы для компании"
    
    def __str__(self):
        return self.name_product 
    