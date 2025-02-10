from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')  # Shows these columns in admin panel

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes')  # Display these fields

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)