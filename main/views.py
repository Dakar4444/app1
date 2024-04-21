from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories



def index(request):
    context = {
        'title': 'Prestige - Главная',
        'content': 'Магазин мебели Prestige',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Prestige - О нас',
        'content': 'О нас',
    }
    return render(request, 'main/about.html', context)

def contact_info(request):
    context = {
        'title': 'Prestige - Контакты',
        'content': 'Контактная информация',
    }
    return render(request, 'main/contact_info.html', context)

def delivery_and_payment(request):
    context = {
        'title': 'Prestige - Доставка и оплата',
        'content': 'Способы доставки и оплаты',
    }
    return render(request, 'main/delivery_and_payment.html', context)