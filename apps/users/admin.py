from django.contrib import admin


from .models import *

admin.site.site_header = "Admin Panel for Mark"
admin.site.index_title="Добро пожаловать"


# Register your models here.
admin.site.register(Register)
admin.site.register(urna)
#admin.site.register(personalarea)
