from django import template
import requests
from django.core.cache import cache

register = template.Library()


@register.filter
def currency_cart(price, currency):
    conversion_set = cache.get('conversion_rates')

    if not conversion_set:
        url = 'https://v6.exchangerate-api.com/v6/74942ad6620965e43cb2afd8/latest/RUB'

        response = requests.get(url)
        data = dict(response.json())

        conversion_set = data['conversion_rates']

        cache.set('conversion_rates', conversion_set, 60 * 60 * 3)


    if currency == 'USD' and 'USD' in conversion_set:
        conversion_rate = conversion_set['USD']
        print(conversion_rate)
        print(price)
        converted_price = round(price * conversion_rate, 2)

        return converted_price

    if currency == 'EUR' and 'EUR' in conversion_set:
        conversion_rate = conversion_set['EUR']
        print(conversion_rate)
        print(price)
        converted_price = round(price * conversion_rate, 2)


        return converted_price

    # Если выбранная валюта не найдена или не поддерживается, возвращаем исходную цену
    return price