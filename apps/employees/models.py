from typing_extensions import Self
from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="фамилия")
    name = models.CharField(max_length=255, verbose_name="имя")
    surname = models.CharField(max_length=255, verbose_name="отчество", blank=True, null=True)#blank null-указывает что строка не обязательная
    date_of_birth =models.DateField(verbose_name="дата рождения")
    email = models.EmailField()
    namber_of_phone = models.CharField(max_length=30, verbose_name="номер телефона")
    class Meta:
        verbose_name = "сотрудники"
        verbose_name_plural = "сотрудники"
        
    @property
    def full_name(self):
        return self.first_name + " --- " + self.name
    
    def __str__(self):
        return self.full_name

class Passport_Data(models.Model):
    employeer = models.ForeignKey(to=Employee, on_delete=models.CASCADE, related_name="passtort_data", verbose_name="Сотрудник")
    inn =models.CharField(max_length=255, verbose_name="ИНН")
    no_passport =models.CharField(max_length=255, verbose_name="Номер паспорта")
    location =models.CharField(max_length=255, verbose_name="место выдачи")
    series =models.CharField(max_length=255, verbose_name="Серия паспорта")
    date_start =models.DateField(max_length=255, verbose_name="Дата получения")
    date_end =models.DateField(max_length=255, verbose_name="Дата окончания")
    class Meta:
        verbose_name = "паспортные данные"
        verbose_name_plural = "паспортные данные"
     
    def passportdate(self):
        return self.employeer
     
    def __str__(self):
        return self.employeer 

    
class Movement (models.Model):
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE, related_name="movement", verbose_name="Сотрудник")
    movement=models.CharField(max_length=255, verbose_name= "должность")
    
    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должность"
        
    def __str__(self):
        return self.employee.full_name

class DriverLicensie (models.Model):
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE, related_name="driverlicensie",verbose_name="Сотрудник")
    category=models.CharField(max_length=30,verbose_name="категория ВУ")
    expirience=models.CharField(max_length=30,verbose_name="Стаж")
    blood=models.CharField(max_length=30,verbose_name="Группа крови")
    date_start_dl=models.CharField(max_length=30,verbose_name="Дата выдачи ВУ")
    date_end_dl=models.CharField(max_length=30,verbose_name="Дата окончания ВУ")
    
    class Meta:
        verbose_name = "водительское удостоверение"
        verbose_name_plural = "водительское удостоверение"
        
    def __str__(self):
        return self.employee.full_name

