from django.http import HttpRequest
from django.template import Library

register = Library()

categories = [
    {'name': 'Футболки', 'url': 't-shirts'},
    {'name': 'Свитшоты', 'url': 'sweatshirts'},
    {'name': 'Худи', 'url': 'hoodies'},
    {'name': 'Рюкзаки', 'url': 'backpacks'},
    {'name': 'Штаны/Шорты', 'url': 'trousers-shorts'},
    {'name': 'Поло', 'url': 'polo'},
    {'name': 'Рубашки', 'url': 'shirts'},
    {'name': 'Пижама', 'url': 'pajamas'},
    {'name': 'Шапки', 'url': 'hats'},
    {'name': 'Кепки', 'url': 'caps'},
    {'name': 'Трусы', 'url': 'underpants'},
    {'name': 'Сувениры', 'url': 'souvenirs'},
    {'name': 'Мемы', 'url': 'memes'},
]


@register.inclusion_tag('shop/header.html')
def get_categories():
    return {'categories': categories}