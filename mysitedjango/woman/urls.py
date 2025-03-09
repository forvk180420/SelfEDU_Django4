"""
В случае, если нужно будет перенести приложение women на другой сайт, то все адреса (path) нужно будет переносить
вручную. Для облегчения django позволяет вместо функции представления воспользоваться функцией include для включения
всех адресов. А саму коллекцию urlpatterns перенести в папку с приложением (woman)
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # http://127.0.0.1:8000/
    path('woman/', views.index),  # http://127.0.0.1:8000/woman/
    path('cats/', views.categories)  # http://127.0.0.1:8000/cats/
]