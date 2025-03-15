"""
При запуске сервера командой:
python manage.py runserver
нет возможности проводить отладку, поэтому нужно сделать свою конфигурацию:

Edit Configurations -> Add New Configuration -> Python

Далее заполняем поля:
name -> mysitedj (Произвольно)
working directory -> ../SelfEDU_Django4/mysitedjango (root) - рабочая директория
Python interpreter -> ../.venv/Scripts/python.exe - путь до интерпретатора
script path -> ../SelfEDU_Django4/mysitedjango/manage.py - путь до manage.py
parameters -> runserver

Теперь можем запускать конфигурацию как в режиме отладке, так и в обычном режиме (без командной строки)

Примечание: командная строка использует по умолчанию powershell.exe, можно в настройках заменить на cmd.exe
"""
