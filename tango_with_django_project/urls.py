"""tango_with_django_project URL Configuration
Here you'll find the mapping of URLs to views within the project. 
This configuration is crucial for defining how URL paths correspond to the Django views they should trigger.
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from rango import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('rango/',include('rango.urls')),
    path('about/', views.about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
