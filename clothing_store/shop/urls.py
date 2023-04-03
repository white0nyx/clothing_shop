from django.urls import path

from shop.views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('registration/', RegistrationPage.as_view(), name='registration'),
    path('logout/', logout_user, name='logout'),
    path('account/', AccountPage.as_view(), name='account'),
    path('category/<slug:category_slug>/', CategoryPage.as_view(), name='category'),
    path('item/<slug:item_slug>/', ItemPage.as_view(), name='item'),
    path('cart', cart_detail, name='cart'),
    path('cart_add/<int:item_id>/', cart_add, name='cart_add'),
]
