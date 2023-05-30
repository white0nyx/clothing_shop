from django import template
import requests
from shop.models import Item
from shop.models import User

register = template.Library()


@register.filter
def currency_cart(price, currency):
    url = 'https://v6.exchangerate-api.com/v6/8a5c33bec501153b4cac56bb/latest/RUB'

    response = requests.get(url)
    data = dict(response.json())

    conversion_set = data['conversion_rates']

    if currency == 'USD' and 'USD' in conversion_set:
        conversion_rate = conversion_set['USD']
        converted_price = round(price * conversion_rate, 2)

        return converted_price

    if currency == 'EUR' and 'EUR' in conversion_set:
        conversion_rate = conversion_set['EUR']
        converted_price = round(price * conversion_rate, 2)

        return converted_price

    # Если выбранная валюта не найдена или не поддерживается, возвращаем исходную цену
    return price