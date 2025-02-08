from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from rango import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
