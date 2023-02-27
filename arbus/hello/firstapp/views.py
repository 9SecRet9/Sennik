#  from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import *
from .forms import UserForm
from django.shortcuts import render

def index(request):
    userform = UserForm()
    return render(request, "firstapp/index.html", {"form": userform})



def index(request):
    if request.method == "POST":
        name = request.POST.get( "name")# получить значение поля Имя
        age = request.POST.get("age")# получить значение поля Возраст
        output = "<h2>Пользователь</h2><h3>Имя - {О}, Возраст - {1}</hЗ>".format(name, age)
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, "firstapp/index.html", {"form": userform})


def index(request):
    cat = ["Ноутбуки", "Принтеры", "Сканеры", "диски", "Шнуры"]
    return render(request, "firstapp/index.html", context={"cat": cat})

def index(request):
    data = {"age": 50}
    return render(request, "firstapp/index.html", context=data)

def index(request):
    return render(request, "firstapp/index.html")


def index(request):
    header = "Персональные данные" # обычная переменная
    langs = ["Английский", "Немецкий", "Испанский"] # массив
    user = {"name": "Максим,", "age": 30} # словарь
    addr = ("Виноградная", 23, 45) # кортеж
    data = { "header": header, "langs": langs, "user": user, "address": addr}
    return render(request, "index.html", context=data)

def index(request):
    # return render(request, "firstapp/home.html")
    data = { "header": "Передача параметров в шаблон Django", "message": "Загружен шаблон templates/firstapp/index_appl.html"}
    return render(request, "firstapp/index_appl.html", context=data)

def index(request):
    return render(request, "firstapp/home.html")

def index(request):
    return HttpResponse("<h2>Главная </h2>")

def about(request):
    return HttpResponse("<h2>0 сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Koнтaкты</h2>")

def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт № {О} Категория: {1}</h2>".format(productid, category)
    return HttpResponse(output)

def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Максим")
    output = "<h2>Пользователь</h2><hЗ>id: {О} Имя: {1}</hЗ >".format(id, name)
    return HttpResponse(output)