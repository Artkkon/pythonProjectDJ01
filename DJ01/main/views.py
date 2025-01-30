from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Главная страница</h1>")

def data(request):
    return HttpResponse("<h1>Разное содержимое</h1>")

def test(request):
    return HttpResponse("<h1>Другое разное содержимое</h1>")
