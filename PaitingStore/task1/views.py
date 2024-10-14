from lib2to3.fixes.fix_input import context
from django.shortcuts import render
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from .models import *

# Create your views here.

def store(requests):
    title = 'Выберите картину'
    Paintin = Painting.objects.all()
    context = {'title': title,
               'Painting':Paintin
               }

    return render(requests, 'store.html', context=context)

def basket(requests):
    title = 'Извините ваша корзина пуста!'
    name = 'Успешный выбор!'
    context = {'title':title,
               'name':name}

    return render(requests, 'basket.html', context=context)

def sign_up_by_html(request):
    users = ['Vital', 'Vitaly', 'Vitalen']
    info = {}
    error = ''
    if request.method == 'POST':
        for key in ('username', 'password', 'password_check', 'age'):
            info[key] = request.POST.get(key, '')

        error = check(info, users)
        if not error:
            return HttpResponse(f'Приветствуем, {info["username"]}')
    return render(request, 'registration_page.html', context={'error': error})

def sign_up_by_django(request):
    users = ['Vital', 'Vitaly', 'Vitalen']
    info = {}
    error = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            for key in ('username', 'password', 'password_check', 'age'):
                info[key] = request.POST.get(key, '')

            error = check(info, users)
            if not error:
                return HttpResponse(f'Приветствуем, {info["username"]}')
        else:
            form = ContactForm()
    return render(request, 'registration_page.html', context={'error': error})

def registration(request):
    return render(request, 'registration_page.html')

def check(info, users):
    if info['password'] != info['password_check']:
        return 'Пароли не совпадают'
    elif int(info['age']) < 18:
        return 'Вы должны быть старше 18'
    elif info['username'] in users:
        return 'Пользователь уже существует'
    return ''
