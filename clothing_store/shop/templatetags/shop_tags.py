from django.http import HttpRequest
from django.template import Library

from shop.models import Category

register = Library()


@register.inclusion_tag('shop/header.html')
def get_categories(category_selected=0):
    return {
        'categories': Category.objects.all(),
        'category_selected': category_selected,
    }
