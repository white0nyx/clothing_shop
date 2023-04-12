from django.template import Library

from shop.models import Category

register = Library()


@register.inclusion_tag('shop/categories_in_header.html')
def get_categories_in_header(category_selected=0):
    return {
        'categories': Category.objects.all(),
        'category_selected': category_selected,
    }


@register.inclusion_tag('shop/categories_in_footer.html')
def get_categories_in_footer(category_selected=0):
    return {
        'categories': Category.objects.all(),
        'category_selected': category_selected,
    }
