from django.contrib import admin
from django.urls import path
from django.urls import include
# from django.conf.urls import url
from rango import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
        path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)