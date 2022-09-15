from typing_extensions import Self
from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob=models.DateField(verbose_name="Дата рождения")
    
