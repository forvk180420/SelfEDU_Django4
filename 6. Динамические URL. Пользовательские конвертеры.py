"""
Если в urls категории
path('cats/', views.categories) http://127.0.0.1:8000/cats/
то может понадобиться разбить категории на подгруппы типа:
http://127.0.0.1:8000/cats/1 или http://127.0.0.1:8000/cats/2 и т.д.

Для этого:
path('cats/<int:cat_id>/', views.categories)
где int - конвертор (в данном случае целое число)
cat_id - переменная целого числа в запросе

А в функцию представления categories нужно добавить переменную cat_id.

Конвертеры URL в Django используются для преобразования частей URL в соответствующие типы данных Python.
Они позволяют определять, как Django должен интерпретировать и обрабатывать различные части URL-адреса.
str - Соответствует любой непустой строке, исключая символ /
int - Соответствует целому числу
slug - Соответствует строке, состоящей из букв, цифр, дефисов и подчеркиваний (my-first-post)
uuid - Соответствует UUID (универсальный уникальный идентификатор) 550e8400-e29b-41d4-a716-446655440000
path - Соответствует любой непустой строке, включая символ / (images/photo.jpg)

Пример slug:
path('cats/<slug:cat_slug>', views.categories_by_slug)  # http://127.0.0.1:8000/cats/my-first-post

Проверка маршрутов (urlpatterns) происходит сверху вниз.

Можно использовать регулярные выражения для маршрутов:
re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive) регулярное выражение архив+год

Можно использовать класс для более удобного представления регулярного выражения:
class FourDigitYearConverter:
    regex = "[0-9]{4}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d" % value

Для удобства использования этот класс следует положить в mysitedjango/woman/converters.py
Далее в файл mysitedjango/woman/urls.py импортируем конвертер:
from . import converters

Затем регистрируем конвертер при помощи функции (в файле mysitedjango/woman/urls.py)
register_converter(converters.FourDigitYearConverter, 'year4'), где year4 - имя конвертера

Затем формируем маршрут:
path("archive2/<year4:year>/", views.archive2)

И функцию представления:
def archive2(request, year):
    return HttpResponse(f"<h1>Архив2 год из 4 цифр</h1><p>{year}</p>")

В классе FourDigitYearConverter строка преобразуется в числовое значение

"""
