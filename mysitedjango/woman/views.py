from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string


def index(request):
    """request - это ссылка на спецкласс, содержащий информацию о запросе: о сессиях, куках и т.д.
    Т.е. через request будет доступна вся информация о текущем запросе"""
    # t = render_to_string('woman/index.html')
    # return HttpResponse(t)  # класс HttpResponse автоматически формирует
    # # нужный заголовок ответа
    return render(request, 'woman/index.html')

def about(request):
    return render(request, 'woman/about.html')

def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id:{cat_id}</p>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Статьи по категориям slug</h1><p>slug:{cat_slug}</p>")


def archive(request, year):
    if int(year) < 2000:
        raise Http404
    # Если год между 2010 и 2015 - то редирект на главную страницу
    elif 2010 < int(year) < 2015:
        return redirect('/')
    # Если год 2017 - то постоянный редирект на главную страницу (код 301)
    elif 2016 < int(year) < 2018:
        return redirect('/', permanent=True)
    # Если год 2009 - то в редирект будут переданы дополнительные параметры (music)
    elif int(year) == 2009:
        return redirect('cat_slug', 'music')
    # Если год 2008 - то в редирект будет передан URL из reverse
    elif int(year) == 2008:
        uri = reverse('cat_slug', args=('reversed_music',))
        return redirect(uri)
    # Если год 2007 - то URL из reverse будет возвращен через HttpResponseRedirect (с кодом 302)
    elif int(year) == 2007:
        uri = reverse('cat_slug', args=('args_HttpResponseRedirect',))
        return HttpResponseRedirect(uri)
    # Если год 2006 - то URL из reverse будет возвращен через HttpResponsePermanentRedirect (с кодом 301)
    elif int(year) == 2006:
        uri = reverse('cat_slug', args=('args_HttpResponsePermanentRedirect',))
        return HttpResponsePermanentRedirect(uri)
    return HttpResponse(f"<h1>Архив</h1><p>{year}</p>")


def archive2(request, year):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Архив2 год из 4 цифр</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
