from django.urls import path

from shop.views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('registration/', RegistrationPage.as_view(), name='registration'),
    path('logout/', logout_user, name='logout'),
    path('account/', AccountPage.as_view(), name='account'),
    path('category/<slug:category_slug>/', CategoryPage.as_view(), name='category'),
    path('item/<slug:item_slug>/', ItemPage.as_view(), name='item'),
    path('cart_add/<int:item_id>/', cart_add, name='cart_add'),
    path('cart_remove/<slug:item_code>/', cart_remove, name='cart_remove'),
    path('place_on_order', place_on_order_page, name='place_on_order'),
    path('payment', payment_page, name='payment'),
    path('change_currency/', change_currency, name='change_currency'),
    path('my_orders/', my_orders, name='my_orders'),
    path('my_orders/<slug:context>', my_orders, name='my_orders'),
    path('chart_page', chart_page, name='chart_page'),
    path('export/products/', export_products_to_csv, name='export_products_to_csv'),
    path('export/users/', export_users_to_csv, name='export_users_to_csv'),
]
