from django.urls import path

from shop.views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('registration/', RegistrationPage.as_view(), name='registration'),
    path('category/<slug:category_slug>', CategoryPage.as_view(), name='category'),
]
