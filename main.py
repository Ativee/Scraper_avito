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
class Url:
    rubric = ''

    def __init__(self, sity = 'blagoveshensk'):
        self.sity = sity
        self.entry_rubric = 'https://2gis.ru/' + sity + '/rubrics'
        self.entry_sity = 'https://2gis.ru/countries/global/' + sity


    # Получение списка городов
    def get_sity_list(self):
        r = requests.get(self.entry_sity)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        # блок областного центра ******
        ul = soup.find_all('li', class_='world__listItem')

        self.sities_links = []
        self.sities_names = []

        for i in ul[0:-18]:
            h2 = i.find('h2', class_='world__listItemName')
            a = h2.find('a')
            a_link = a.get('href')
            abs_link = 'https://2gis.ru' + a_link + '/rubrics'
            self.sities_links.append(abs_link)
            self.sities_names.append(h2.string)
            # print(h2.string)
            # print(abs_link)



    # запись списка городов в базу данных
    # def rec_sity_list(self):
        con = lite.connect('C:\\Users\\Елагин\\PycharmProjects\\Scraper_avito\\GIS.db')
    #     with con:
    #         cur = con.cursor()
    #         try:
    #
    #         cur.execute("INSERT INTO Sities_list (sity) VALUES('hhhh')")
    #         # cur.execute("INSERT INTO Sities_list VALUES(link=:link, link )", {"sity": self.sity})
    #         con.commit()
    #     print('запись произведена')


# def rec(arg):
#     con = lite.connect('C:\\Users\\Елагин\\PycharmProjects\\Scraper_avito\\GIS.db')
#
#     cur = con.cursor()
#
#     cur.execute("INSERT INTO Sities_list (sity) VALUES(?)", str(arg))
#             # cur.execute("INSERT INTO Sities_list VALUES(link=:link, link )", {"sity": self.sity})
#     con.commit()
#     print('запись произведена')
#     cur.close()
#     con.close()



def main():
    print(os.getcwd())

    a = Url()
    print(a.entry_sity)
    a.get_sity_list()
    print(len(a.sities_links))
    print(a.sities_links)
    print(len(a.sities_names))
    print(a.sities_names)
    for sity in a.sities_names:
        print(sity)
        rec(sity)














if __name__ == '__main__':
    main()






