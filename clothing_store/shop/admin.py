from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug', 'description', 'price',
                    'date_create', 'date_update', 'is_in_stock')
    list_display_links = ('name',)
    list_editable = ('is_in_stock',)
    list_filter = ('category', 'date_update', 'is_in_stock')
    search_fields = ('name', 'category',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
