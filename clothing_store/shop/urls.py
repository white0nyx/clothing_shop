from django.urls import path

from shop.views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('registration/', RegistrationPage.as_view(), name='registration'),
    path('logout/', logout_user, name='logout'),
    path('account/', AccountPage.as_view(), name='account'),
    path('category/<slug:category_slug>/', CategoryPage.as_view(), name='category'),
    path('item/<slug:item_slug>/', ItemPage.as_view(), name='item'),
    path('cart', cart, name='cart'),
    path('add_to_cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
]
