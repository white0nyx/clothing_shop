from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home_page(request: HttpRequest):
    return HttpResponse('<h1>Главная страница магазина одежды<h1>')
