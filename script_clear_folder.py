#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from getpass import getuser
from shutil import rmtree
from shutil import copy2
from time import sleep

try:
# Проверяем первый ли это запуск и добавляем в автозагрузку
    is_first = True
    if os.path.isfile(os.getenv("APPDATA") + '\\Microsoft\\Windows\\Start Menu\\Programs\\Startup' + '\ '[0] + os.path.basename(sys.argv[0])) is False:
        copy2(sys.argv[0], os.getenv("APPDATA") + '\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    else:
        is_first = False

    name = getuser() # Узнаем имя пользователя
    folder = "esoft" # Папка, где будем удалять файлы
    path_to_folder = "C:\\Users\\" + str(name) + "\\" + str(folder) # Узнаем путь до папки, моя папка находится по адресу "C:\Users\admin\esoft",
    basedir = os.path.abspath(path_to_folder) # Абсолютный путь до папки

    while True:
        path_f = []
        t = []
        total_size = 0

        for d, dirs, files in os.walk(basedir): # найдем расположение каждого файла в папке "esoft"
            for f in files:
                path = os.path.join(d,f) # формирование адреса
                path_f.append(path) # добавление адреса в список
        for p in path_f:
            getsize = os.path.getsize(p) # смотрим размер каждого файла
            t.append(getsize) # записываем в конец пустого списка t все размеры файлов

        for size in t: # Извлекаем из списка t размеры и заносим в переменную size
            total_size += int(size) # Выполняем сложение всех файлов в папке "esoft", на выходе получем общий объем папки

        if total_size >= 50000000: # Если размер папки "esoft" больше или равен 50 MB, то чистим папку
            rmtree(basedir + "\\", ignore_errors = True)
        sleep(1800)
except Exception as e:
    pass
