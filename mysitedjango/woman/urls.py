"""
В случае, если нужно будет перенести приложение women на другой сайт, то все адреса (path) нужно будет переносить
вручную. Для облегчения django позволяет вместо функции представления воспользоваться функцией include для включения
всех адресов. А саму коллекцию urlpatterns перенести в папку с приложением (woman)
"""
from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),  # http://127.0.0.1:8000/
    path('woman/', views.index, name='woman'),  # http://127.0.0.1:8000/woman/
    path('about/', views.about, name='about'),
    path('cats/<int:cat_id>/', views.categories, name='cat_id'),  # http://127.0.0.1:8000/cats/
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cat_slug'),
    # http://127.0.0.1:8000/cats/my-first-post
    re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive, name='archive'),  # регулярное выражение архив+год
    path("archive2/<year4:year>/", views.archive2, name='archive2'),  # регулярное выражение архив2+год
    path('send-dif-type/', views.send_dif_type, name='send_dif_type')
]
