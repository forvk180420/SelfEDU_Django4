from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """request - это ссылка на спецкласс, содержащий информацию о запросе: о сессиях, куках и т.д.
    Т.е. через request будет доступна вся информация о текущем запросе"""
    return HttpResponse("Страница приложения women")  # класс HttpResponse автоматически формирует
    # нужный заголовок ответа


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id:{cat_id}</p>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Статьи по категориям slug</h1><p>slug:{cat_slug}</p>")


def archive(request, year):
    return HttpResponse(f"<h1>Архив</h1><p>{year}</p>")


def archive2(request, year):
    return HttpResponse(f"<h1>Архив2 год из 4 цифр</h1><p>{year}</p>")
