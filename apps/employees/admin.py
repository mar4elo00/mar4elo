from django.contrib import admin
from .models import *

admin.site.site_header = "Admin Panel for Mark"
admin.site.index_title="Добро пожаловать"


# Register your models here.
admin.site.register(Employee)
admin.site.register(Movement)
admin.site.register(DriverLicensie)
admin.site.register(Passport_Data)
