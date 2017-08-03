from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import sys
import os
import lxml


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

# Генерация URL для парсинга страницы
class Page_url:
    url = 'https://www.2gis.ru/'
    city = ''
    rubric = 'rubrics'

# Генерация URL для парсинга страницы
    def __init__(self, city = 'blagoveshensk'):
        self.city = city
        self.url = self.url + city + '/' + self.rubric
#  извлечение данных
# https://2gis.ru/blagoveshensk/rubrics
class pars:
    pass

def main():
    html = Page_url()
    # page = (requests.get(html.url)
    # soup = BeautifulSoup(page.read())
    # print(page)
    # print(html.url)
    html_soup = urlopen(html.url)
    bsObj = BeautifulSoup(html_soup.read(), "html.parser")
    h3 = bsObj.find_all('h3',)
    for i in h3:
        print(i)


    # print(bsObj)






    # entry = Page_url()
    # print(entry.url)
    # r = requests.get(entry.url)
    #
    # soup = BeautifulSoup(r,'lxml')
    # print(soup)
    # print(r.text)




if __name__ == '__main__':
    main()






