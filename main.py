from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml
import sqlite3 as lite
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
        # блок областного центра ******
        ul = soup.find_all('li', class_='world__listItem')
        print(len(ul))
        self.sity_link = []
        self.sity_name = []

        for i in ul[0:-18]:
            h2 = i.find('h2',class_='world__listItemName')
            a = h2.find('a')
            a_link = a.get('href')
            abs_link = 'https://2gis.ru' + a_link + '/rubrics'
            self.sity_link.append(abs_link)
            self.sity_name.append(h2.string)
            # print(h2.string)
            # print(abs_link)

    def rec_sity_list(self):
        con = lite.connect('C:\\Users\\Елагин\\PycharmProjects\\Scraper_avito\\GIS.db')
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO Sities_list (sity) VALUES('hhhh')")
            # cur.execute("INSERT INTO Sities_list VALUES(link=:link, link )", {"sity": self.sity})
            con.commit()

        print('запись произведена')









        # for i in li:
        #     h2 = i.find('h2', class_="world__listItemName")
        #
        #
        #     print(h2)

            # h2_a = h2.find('a')
            # link = h2_a.get('href')
            # li_sat = i.find_all('li', class_='world__settlementsItem')
            # print('Областной центр: ', h2_text, 'Ссылка: ', link)
            # for i in li_sat:
            #     if li_sat is None:
            #         print("Нет городов сателитов")
            #     else:
            #         i.find_all('a')
            #         for z in i:
            #             print(z)
            #         print(len(z))

            # print('',li_sat)




def main():
    a = Url()
    print(a.entry_sity)
    a.get_sity_list()
    a.rec_sity_list()
    print (a.sity_link[0:5])









if __name__ == '__main__':
    main()






