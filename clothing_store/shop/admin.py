from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm

from .forms import RegisterUserForm
from .models import *


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = RegisterUserForm

    list_display = ('username', 'email', 'first_name', 'last_name', 'father_name', 'phone', 'country', 'city', 'address',
                    'post_index', 'region', 'is_superuser', 'date_joined', )
    list_filter = ('is_superuser', 'is_staff')


    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Личная информация', {'fields': ('first_name', 'last_name', 'username')}),
        ('Права', {'fields': ('is_superuser', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
         ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


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


class ImageItemAdmin(admin.ModelAdmin):
    list_display = ('path', )
    list_display_links = ('path',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'email', 'date_create', 'date_update', 'status')
    list_display_links = ('user_id', )
    list_editable = ('status', )
    list_filter = ('user_id', 'status', 'date_create', 'date_update')
    search_fields = ('user_id', 'email')

class LinkinOrdersAndItemsAdmin(admin.ModelAdmin):
    list_display = ('order', 'item')
    list_display_links = ('order', 'item')
    search_fields = ('order', 'item')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(AdditionalImageItem, ImageItemAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(LinkinOrdersAndItems, LinkinOrdersAndItemsAdmin)
