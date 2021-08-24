from django.shortcuts import render, redirect


def index(request):
    data = {
        'title': 'Главная страница',
    }

    return render(request, 'agugai/index.html',data)
