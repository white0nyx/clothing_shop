from django.urls import path

from shop.views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('registration/', RegistrationPage.as_view(), name='registration'),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('category/<slug:category_slug>', CategoryPage.as_view(), name='category'),
]
