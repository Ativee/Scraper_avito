import Parsing
from bs4 import BeautifulSoup
import re

from tkinter import *
import sqlite3 as lite
import os
import requests
import sys
import Window

"""
Парсинг сайта 2ГИС для составления базы данных огранизаций 

Алгоритм извлечения данных:

1. Парсинг первой страницы сайта для составления
    - рубрикатора
    - списка городов
    - парсинг подрубрик по городам
    
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
class Form:
    def __init__(self):
        self.root = Tk()
        self.root.title('Форма для ответа')
        self.root.geometry('500x400+300+200')
        self.width = 50


class Question:
    def __init__(self, form, question):
        self.lab = Label(form.root, text=question)
        self.ent = Entry(form.root, width=form.width + 16)
        self.lab.pack()
        self.ent.pack()


class BigQuestion:
    def __init__(self, form, question):
        self.lab = Label(form.root, text=question)
        self.txt = Text(form.root, width=form.width, height=4)
        self.lab.pack()
        self.txt.pack()


class RadioBut:
    def __init__(self, form, question):
        self.lab = Label(form.root, text=question)
        self.lab.pack()
        self.var = IntVar()
        self.var.set(1)
        self.rad0 = Radiobutton(form.root, text="0-9", variable=self.var, value=9)
        self.rad1 = Radiobutton(form.root, text='10-19', variable=self.var, value=19)
        self.rad2 = Radiobutton(form.root, text='20-29', variable=self.var, value=29)
        self.rad3 = Radiobutton(form.root, text='30-39', variable=self.var, value=39)
        self.rad0.pack()
        self.rad1.pack()
        self.rad2.pack()
        self.rad3.pack()


class Flags:
    def __init__(self, form, question):
        self.lab = Label(form.root, text=question)
        self.lab.pack()
        self.c0 = IntVar()
        self.c1 = IntVar()
        self.c2 = IntVar()
        self.c3 = IntVar()
        self.che0 = Checkbutton(form.root, text="Красный", bg='red',
                                variable=self.c0, onvalue=1, offvalue=0)
        self.che1 = Checkbutton(form.root, text="Синий", bg='blue',
                                variable=self.c1, onvalue=1, offvalue=0)
        self.che2 = Checkbutton(form.root, text="Зелёный", bg='green',
                                variable=self.c2, onvalue=1, offvalue=0)
        self.che3 = Checkbutton(form.root, text="Жёлтый", bg='yellow',
                                variable=self.c3, onvalue=1, offvalue=0)
        self.che0.pack()
        self.che1.pack()
        self.che2.pack()
        self.che3.pack()


class Scene:
    def __init__(self):
        self.form = Form()
        self.qstn = Question(self.form, 'Ваш адрес:')
        self.comm = BigQuestion(self.form, 'Комментарий:')
        self.radi = RadioBut(self.form, 'Сколько штук?')
        self.flag = Flags(self.form, 'Какого цвета?')
        self.butt = Button(self.form.root, text='Отправить')
        self.butt.pack()
        self.butt.bind('<Button-1>', self.go)
        self.form.root.mainloop()

    def go(self, event):
        print('Send:\n',
              'Colors:', self.flag.c0.get(), self.flag.c1.get(),
              self.flag.c2.get(), self.flag.c3.get(),
              'Count:', self.radi.var.get(),
              'Text:', self.qstn.lab.g)






#


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
        return list

    def Spisok_sity():
        for i in Selecting_all():
            print(i[0:2])
        print("ВВЕДИТЕ НОМЕР ГОРОДА\n")


    def Selecting_one(sity_id):

        con = lite.connect(str(os.getcwd() + '\GIS.db'))
        cur = con.cursor()
        cur.execute("SELECT * FROM Sities_list WHERE id=?", (sity_id,))
        row = cur.fetchall()
        return row[0]



    if mode == 1:
        Selecting_all()
        print('Список городов загружен. Всего: ', len(Selecting_all()), 'городов')


    elif mode == 2:
        Spisok_sity()
        sity_id = int(input())
        print('Выбранный вами город:',Selecting_one(sity_id)[0] )


    elif mode == 3:
        Spisok_sity()
        sity_id = int(input())
        print('Выбранный вами город:', Selecting_one(sity_id)[0])
def Selecting_main_rubric(mode):
    def Selecting_all():
        list = []
        con = lite.connect(str(os.getcwd() + '\GIS.db'))
        cur = con.cursor()
        cur.execute('SELECT * FROM Main_rubricks')
        for i in cur.fetchall():
            list.append(i)

        return list

    def maim_rubric_spisok():
        for i in Selecting_all():
            print(i[1:3])
        print("Введите норер основной рубрики\n")

    def Selecting_one(main_rubric_id):
        con = lite.connect(str(os.getcwd() + '\GIS.db'))
        cur = con.cursor()
        cur.execute("SELECT * FROM Main_rubricks WHERE id=?", (main_rubric_id,))
        row = cur.fetchall()
        return row


    if mode == 1:
        maim_rubric_spisok()
        main_rubric_id = int(input())
        print('Выбранная вами рубрика:', Selecting_one(main_rubric_id)[0][2])



    elif mode == 2:
        Selecting_all()
        print('Список основных рубрик загружен. Всего: ', len(Selecting_all()), 'основных рубрик')



    elif mode == 3:
        maim_rubric_spisok()
        main_rubric_id = int(input())
        print('Выбранная вами рубрика:', Selecting_one(main_rubric_id)[0][2])



    # def get_url(mode):
    #     print(mode)
    #
def window_mode(mode):
    if mode ==2:
        start(mode)
        Selecting_sities(mode)
        Selecting_main_rubric(mode)
    elif mode ==1:
        start(mode)
        Selecting_main_rubric(mode)
        Selecting_sities(mode)
    elif mode ==3:
        start(mode)
        Selecting_main_rubric(mode)
        Selecting_sities(mode)
    else:
        restart()

#
# def Parsing_sub_rubric():
#     def make_url_mode_1():
#         for i in Selecting_sities(1):
#             print(i)
#     make_url_mode_1()




def main():
    scene = Scene()

    main_window()

    Privetstvie()
    mode = int(input())
    window_mode(mode)

    # Parsing_sub_rubric()


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






