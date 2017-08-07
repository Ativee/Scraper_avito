from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml
import sqlite3
import os
import requests

"""
Парсинг сайта 2ГИС для составления базы данных огранизаций 

Алгоритм извлечения данных:

1. Парсинг первой страницы сайта для составления
    - рубрикатора
    - списка городов
    
2. Структура извлекаемых данных:
    - Город
    - Наименование огранизации
    - Номер телефона
    - Адресс
    - E-mail
    - Сайт
    - Смежные рубрики
    - Режим работы

3. Запись экземпляра класса в базу данных.
4. Потроение API для работы с базой данных.


Алгоритм отслеживания изменений и тенденций:

1. Проверка количества организаций по рубрикам
2. Сводка открывшихся и закрывшихся организаций
3. Сводка организаций проводящих рекламную компанию


"""
#  список городов              https://2gis.ru/countries/global/blagoveshensk
# спиок рубрик внутри города   https://2gis.ru/blagoveshensk/rubrics
# Генерация URL для парсинга страницы
class Url:
    rubric = ''
    def __init__(self, sity = 'blagoveshensk'):
        self.sity = sity
        self.entry_rubric = 'https://2gis.ru/' + sity + '/rubrics'
        self.entry_sity = 'https://2gis.ru/countries/global/' + sity

    def get_sity_list(self):
        r = requests.get(self.entry_sity)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.find_all('ul', class_='world__list')
        print(ul)






def main():
    a = Url()
    print(a.entry_sity)
    a.get_sity_list()








if __name__ == '__main__':
    main()






