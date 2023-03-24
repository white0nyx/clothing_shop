from django.urls import path

from shop.views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('accounts/profile/', HomePage.as_view(), name='profile'), # чтобы не было 404 ошибки при авторизации
    path('registration/', RegistrationPage.as_view(), name='registration'),
    #path('login/', LoginPage.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('account/', AccountPage.as_view(), name='account'),
    path('category/<slug:category_slug>/', CategoryPage.as_view(), name='category'),
    path('item/<slug:item_slug>/', ItemPage.as_view(), name='item'),
]
