from django.contrib import admin

from apps.users.views import register
from .models import *

admin.site.site_header = "Admin Panel for Mark"
admin.site.index_title="Добро пожаловать"


# Register your models here.
admin.site.register(Register)
