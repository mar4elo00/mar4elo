from typing_extensions import Self
from django.db import models
from django.contrib.auth.models import User
from apps.product.models import *

class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob=models.DateField(verbose_name="Дата рождения")
    
class Urna(models.Model):
    user=models.ForeignKey(to=User, on_delete=models.CASCADE , related_name="cart",verbose_name="Пользователь")
    name_product=models.ForeignKey(to=Products, on_delete=models.CASCADE, related_name="prod",verbose_name="Товар")
    summ=models.CharField(max_length=255,verbose_name="Количество",blank=True,null=True)
    
#class personalarea(models.Model):
    