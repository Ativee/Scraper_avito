from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml
import sqlite3 as lite
import os
import requests
import sys

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
def get_sities_links(arg):
    con = lite.connect('C:\\Users\\Елагин\\PycharmProjects\\Scraper_avito\\GIS.db')
    cur = con.cursor()

    cur.execute('SELECT ? FROM Sities_list', arg)
    print(cur.fetchall())


class Url:
    rubric = ''

    def __init__(self, sity = 'blagoveshensk'):
        self.sity = sity
        self.siti_list = get_sities_links('sity')

        # self.entry_rubric = 'https://2gis.ru/' + sity + '/rubrics'
        # self.entry_sity = 'https://2gis.ru/countries/global/' + sity


    # Получение списка городов
    # def get_sity_list(self):
    #     r = requests.get(self.entry_sity)
    #     html = r.text
    #     soup = BeautifulSoup(html, 'html.parser')
    #     # блок областного центра ******
    #     ul = soup.find_all('li', class_='world__listItem')
    #
    #     self.sities_links = []
    #     self.sities_names = []
    #     self.sities_urls =[]
    #
    #     for i in ul[0:-18]:
    #         h2 = i.find('h2', class_='world__listItemName')
    #         a = h2.find('a')
    #         a_link = a.get('href')
    #         abs_link = 'https://2gis.ru' + a_link + '/rubrics'
    #         sity_url = {'syti': h2.string, 'sity_link': abs_link }
    #         self.sities_links.append(abs_link)
    #         self.sities_names.append(h2.string)
    #         self.sities_urls.append(sity_url)
    #         # print(h2.string)
    #         # print(abs_li


#
# # запись списка городов в базу данных
# def rec(a,b):
#     con = lite.connect('C:\\Users\\Елагин\\PycharmProjects\\Scraper_avito\\GIS.db')
#     cur = con.cursor()
#     c = (a, b)
#     cur.execute('INSERT INTO Sities_list (sity,link) VALUES(?,?)', c)
#     con.commit()
#     print(c)
#     cur.close()
#     con.close()

#

def main():

    all_sity = Url()
    print(Url.siti_list)














if __name__ == '__main__':
    main()






