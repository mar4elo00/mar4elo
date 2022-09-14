from django import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from . import views

urlpatterns = [
    path("",ONOXOview,name='home'),
    path("home/",ONOXOview,name='homes'),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
