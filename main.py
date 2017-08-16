
from bs4 import BeautifulSoup
import re

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

# # Генерация URL для парсинга страницы
#
# def get_sities_links():
#
#     con = lite.connect('C:\\Users\\Елагин\\PycharmProjects\\Scraper_avito\\GIS.db')
#     cur = con.cursor()
#     cur.execute('SELECT id,link FROM Sities_list')
#     # print(cur.fetchall())
#     return cur.fetchall()
#
#
# def get_rubpic(url):
#     r = requests.get(url).text
#     soup = BeautifulSoup(r, "html.parser")
#     li = soup.find_all('li', class_='rubricsList__listItem')
#     data = []
#     rubric_data = []
#
#     for rubr in li:
#         rub = rubr.find('h3')
#         href = rub.find('a').get('href')
#         text = rub.find('a').text
#         result = re.split(r'/',href, maxsplit=3)[-1]
#
#
#         # print(text,'   Идентификатор рубрики:', int(result) )
#         data = [text, int(result),href]
#
#         rubric_data.append(data)
#
#     return rubric_data
#
# def rec_main_rubrick(gis_id, rubr_name,link):
#     con = lite.connect('C:\\Users\\Елагин\\PycharmProjects\\Scraper_avito\\GIS.db')
#     cur = con.cursor()
#     cur.execute('INSERT INTO Main_rubricks(name,id_gis,Link) VALUES (?,?,?)',(gis_id, rubr_name,link))
#     con.commit()
#     con.close()
#
#
#
# class Url:
#     rubric = ''
#     f = get_sities_links()
#
#     def __init__(self, sity = 'blagoveshensk'):
#         self.sity = sity
#         self.bd_sities = []
#         # self.entry_rubric = 'https://2gis.ru/' + sity + '/rubrics'
#         # self.entry_sity = 'https://2gis.ru/countries/global/' + sity
#         # Получение списка городов
#         # def get_sity_list(self):
#         #     r = requests.get(self.entry_sity)
#         #     html = r.text
#         #     soup = BeautifulSoup(html, 'html.parser')
#         #     # блок областного центра ******
#         #     ul = soup.find_all('li', class_='world__listItem')
#         #
#         #     self.sities_links = []
#         #     self.sities_names = []
#         #     self.sities_urls =[]
#         #
#         #     for i in ul[0:-18]:
#         #         h2 = i.find('h2', class_='world__listItemName')
#         #         a = h2.find('a')
#         #         a_link = a.get('href')
#         #         abs_link = 'https://2gis.ru' + a_link + '/rubrics'
#         #         sity_url = {'syti': h2.string, 'sity_link': abs_link }
#         #         self.sities_links.append(abs_link)
#         #         self.sities_names.append(h2.string)
#         #         self.sities_urls.append(sity_url)
#         #         # print(h2.string)
#         #         # print(abs_li
# # def rec(a,b):
# #     con = lite.connect('C:\\Users\\Елагин\\PycharmProjects\\Scraper_avito\\GIS.db')
# #     cur = con.cursor()
# #     c = (a, b)
# #     cur.execute('INSERT INTO Sities_list (sity,link) VALUES(?,?)', c)
# #     con.commit()
# #     print(c)
# #     cur.close()
# #     con.close()
#
# #
#
# def rubrics_list():
#     con = lite.connect('C:\\Users\\Елагин\\PycharmProjects\\Scraper_avito\\GIS.db')
#     cur = con.cursor()
#     cur.execute('SELECT id, id_gis FROM Main_rubricks')
#     # print(cur.fetchall())
#     return cur.fetchall()
#     pass
#
# def Bla(url):
#     # url = 'https://2gis.ru/noyabrsk/rubrics/subrubrics/42903'
#     r = requests.get(srt(url)).text
#
#     div = BeautifulSoup(r, "html.parser")
#     diiv = div.find_all('div', class_='rubricsList__content')
#     # li = diiv.find_all('li', class_='rubricsList__listItem')
#
#     print('Количество дивов с классом ',len(diiv))
#     # print(diiv[-1])
#     soup = BeautifulSoup(str(diiv[-1]),"html.parser")
#     li = soup.find_all('li', class_='rubricsList__listItem')
#     result = []
#     for i in li:
#         # rub = i.find('h3')
#         href = i.find('a').get('href')
#         text = i.find('a').text
#         # print(rub)
#         # print(href)
#         # print(text)
#         data = [href,text]
#
#         result.append(data)
#         # print('   ')
#     # print(result)
#     # print(len(result))
#     return result
#
#
#
#
#
#
#
#         # print(i)
#
#
#
#
#
#     # li = soup.find_all('li', class_='rubricsList__listItem')
#     # data = []
#     # rubric_data = []
#
#     # for rubr in li:
#     #     print(rubr)
#     #     # rub = rubr.find('h3')
#     #     # href = rub.find('a').get('href')
#     #     # text = rub.find('a').text
#     #     # result = re.split(r'/', href, maxsplit=3)[-1]
#     #
#     #
#     #     # print(text,'   Идентификатор рубрики:', int(result) )
#     #     # data = [text, int(result), href]
#     #     # print(data)


def Privetstvie():
    print('Программа парсинга сайта 2гис запущена.')
    print('Выберите предложенный режим использования программы:')
    mode_1 = 'Фильтр компаний по рубрикам'
    print('1. ', mode_1)
    mode_2 = 'Фильтр компаний по городам'
    print('2. ', mode_2)
    mode_3 = 'Фильтр компаний по рубрикам и городам'
    print('3. ', mode_3)

def restart():
    start()

def start(mode):
    if mode == 1:
        print('ВЫБРАННЫЙ РЕЖИМ №',mode,':')

    elif mode == 2:
        print('ВЫБРАННЫЙ РЕЖИМ №',mode,':')

    elif mode == 3:
        print('ВЫБРАННЫЙ РЕЖИМ №',mode,':')

    else:
        print('Вы ввели неправильный параметр попробуйте еще раз\n\n\n')
        restart()






    #     id_sity = input('Введите id города показанный в таблице\n')
    #     cur.execute('SELECT * FROM Sities_list WHERE id=?',id_sity)
    #
    #     print('Выбранный вами город: ', cur.fetchall())
    #
    #
    #
    # con.commit()
    # con.close()

def Selecting_sities(mode):
    def Selecting_all():
        list = []
        con = lite.connect(str(os.getcwd() + '\GIS.db'))
        cur = con.cursor()
        cur.execute('SELECT * FROM Sities_list')
        for i in cur.fetchall():
            list.append(i)
        print('Список городов загружен. Всего: ',len(list), 'городов')
        return list
    def Selecting_one():
        for i in Selecting_all():
            print(i[0:2])
        print("Введите норер города\n")

        con = lite.connect(str(os.getcwd() + '\GIS.db'))
        cur = con.cursor()
        # sity = input()
        cur.execute("SELECT * FROM Sities_list ")

        print('Выбранный вами город:', cur.fetchall())



    if mode == 1:
        Selecting_all()


    elif mode == 2:
        Selecting_one()

    elif mode == 3:
        Selecting_one()


def main():
    Privetstvie()
    # mode = int(input())
    # start(mode)
    Selecting_sities(mode=2)







    # katalog_sity = Url()
    # sities_list = katalog_sity.f
    # print(len(sities_list))
    #
    # Bla()
    #
    #
    #
    # for sity in sities_list:
    #     url = str(sity[-1]) + '/subrubrics/'
    #     for rubrica in rubrics_list():
    #         b = url + str(rubrica[-1])
    #         print(b)
    #         Bla(b)
    #         print(Bla()[-1])
    #


            #  ЗАПИСЬ ПАРАМЕТРОВ В БАЗУ ДАННЫХ
            # con = lite.connect('C:\\Users\\Елагин\\PycharmProjects\\Scraper_avito\\GIS.db')
            # cur = con.cursor()
            # cur.execute('INSERT INTO Sub_rubrics (Sity,Parent_rubric,Sub_rubric_name,Sub_rubric_link) VALUES (?,?,?,?)', (sity[0], rubrica[0], link))
            # con.commit()
            # con.close()







        # print(sity[-1])

if __name__ == '__main__':
    main()






