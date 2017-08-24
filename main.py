import Parsing
from bs4 import BeautifulSoup
import re
from tkinter import *
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
        self.m = self.root.config()
        self.root.title('Программа парсинга 2ГИС')
        self.root.geometry('800x600+50+50')
        self.width = 50



class Menushka:
    def __init__(self, form):
        self.m = Menu(form)
        form.config(menu=self.m)
        self.fm = Menu(self.m)  # создается пункт меню с размещением на основном меню (m)
        self.m.add_cascade(label="Парсинг", menu=self.fm)  # пункту располагается на основном меню (m)
        self.fm.add_command(label="Открыть из...")  # формируется список команд пункта меню
        self.fm.add_command(label="Новый проект")
        self.fm.add_command(label="Сохранить...")
        self.fm.add_command(label="Выход")

        self.db = Menu(self.m)  # создается пункт меню с размещением на основном меню (m)
        self.m.add_cascade(label="База данных", menu=self.db)  # пункту располагается на основном меню (m)
        self.db.add_command(label="Открыть...")  # формируется список команд пункта меню
        self.db.add_command(label="Новый из парсинга")
        self.db.add_command(label="Записать...")

class Create_label:
    def __init__(self,form,text):
        self.lab = Label(form)
        self.lab['text'] = text
        self.lab.grid(row=1, column=2, columnspan=1)

class Create_radio_but:
    def __init__(self, form,question):
        self.lab = Label(form.root, text=question)
        self.lab.grid(row=1, column=0, columnspan=3, sticky='w')
        self.var = IntVar()
        self.var.set(1)
        self.rad0 = Radiobutton(form.root, text="По рубрикам", variable=self.var,value=1)
        self.rad1 = Radiobutton(form.root, text="По городам", variable=self.var,value=2)
        self.rad2 = Radiobutton(form.root, text="По рубрикам и городам", variable=self.var,value=3)
        self.rad0.grid(row=2, column=0)
        self.rad1.grid(row=2, column=1)
        self.rad2.grid(row=2, column=2)

class Pars_param_sity_frame:
    def __init__(self,form):
        self.fr1 = Frame(form,width=400,height=200,bg="#CDC9C9")
        self.fr1.grid(row=3,column=0,columnspan=2)

class Pars_param_rubrick_frame:
    def __init__(self,form):
        self.fr2 = Frame(form,width=400,height=200,bg="#8B8989")
        self.fr2.grid(row=3,column=2,columnspan=2)

class Sity_list_box:

    def __init__(self):

    def Selecting_sities(mode):





class Scene:
    def __init__(self):
        self.form = Form()
        # создаю меню
        self.menu = Menushka(self.form.root)
        # Создаю группу радиокнопок
        self.radi = Create_radio_but(self.form,'Выбрать режим парсинга')
        # Создаю кнопку для отправки результата из группы
        self.Send_pars_param = Button(self.form.root, text='Включить режим парсинга')
        # Позиционирую кнопку
        self.Send_pars_param.grid(row=2, column=3, sticky='e')
        # Связываю нажатие на кнопку с  функцией *** Pars_param_func ***
        self.Send_pars_param.bind('<Button-1>', self.Pars_param_func)
        # Создаю основной фрейм для отображения списков рубрик и городов
        self.fr_sity = Pars_param_sity_frame(self.form.root)
        # Создаю два подфрейма для
        # №1 для отображения списка городов
        # №2 для отображения списка рубрик
        # №3 появление данных фреймов регулируется функцией: ***  ***
        self.sity_fr = Pars_param_rubrick_frame(self.form.root)







        self.form.root.mainloop()
    # Функция обрабатывает результат выбора режима парсинга
    # работает от *** Send_pars_param ***
    def Pars_param_func(self, event):
        self.sel =self.radi.var.get()
        if self.sel == 1:
            print(self.sel)
        elif self.sel == 2:
            print(self.sel)
        elif self.sel == 3:
            print(self.sel)




    #










# def Privetstvie():
#     print('Программа парсинга сайта 2гис запущена.')
#     print('Выберите предложенный режим использования программы:')
#     mode_1 = 'Фильтр компаний по рубрикам'
#     print('1. ', mode_1)
#     mode_2 = 'Фильтр компаний по городам'
#     print('2. ', mode_2)
#     mode_3 = 'Фильтр компаний по рубрикам и городам'
#     print('3. ', mode_3)
# def restart():
#     start()
# def start(mode):
#     if mode == 1:
#         print('ВЫБРАННЫЙ РЕЖИМ №',mode,':')
#
#     elif mode == 2:
#         print('ВЫБРАННЫЙ РЕЖИМ №',mode,':')
#
#     elif mode == 3:
#         print('ВЫБРАННЫЙ РЕЖИМ №',mode,':')
#
#     else:
#         print('Вы ввели неправильный параметр попробуйте еще раз\n\n\n')
#         restart()
#
#
#
#
#
#
#     #     id_sity = input('Введите id города показанный в таблице\n')
#     #     cur.execute('SELECT * FROM Sities_list WHERE id=?',id_sity)
#     #
#     #     print('Выбранный вами город: ', cur.fetchall())
#     #
#     #
#     #
#     # con.commit()
#     # con.close()
#
# def Selecting_sities(mode):
#     def Selecting_all():
#         list = []
#         con = lite.connect(str(os.getcwd() + '\GIS.db'))
#         cur = con.cursor()
#         cur.execute('SELECT * FROM Sities_list')
#         for i in cur.fetchall():
#             list.append(i)
#         return list
#
#     def Spisok_sity():
#         for i in Selecting_all():
#             print(i[0:2])
#         print("ВВЕДИТЕ НОМЕР ГОРОДА\n")
#
#
#     def Selecting_one(sity_id):
#
#         con = lite.connect(str(os.getcwd() + '\GIS.db'))
#         cur = con.cursor()
#         cur.execute("SELECT * FROM Sities_list WHERE id=?", (sity_id,))
#         row = cur.fetchall()
#         return row[0]
#
#
#
#     if mode == 1:
#         Selecting_all()
#         print('Список городов загружен. Всего: ', len(Selecting_all()), 'городов')
#
#
#     elif mode == 2:
#         Spisok_sity()
#         sity_id = int(input())
#         print('Выбранный вами город:',Selecting_one(sity_id)[0] )
#
#
#     elif mode == 3:
#         Spisok_sity()
#         sity_id = int(input())
#         print('Выбранный вами город:', Selecting_one(sity_id)[0])
# def Selecting_main_rubric(mode):
#     def Selecting_all():
#         list = []
#         con = lite.connect(str(os.getcwd() + '\GIS.db'))
#         cur = con.cursor()
#         cur.execute('SELECT * FROM Main_rubricks')
#         for i in cur.fetchall():
#             list.append(i)
#
#         return list
#
#     def maim_rubric_spisok():
#         for i in Selecting_all():
#             print(i[1:3])
#         print("Введите норер основной рубрики\n")
#
#     def Selecting_one(main_rubric_id):
#         con = lite.connect(str(os.getcwd() + '\GIS.db'))
#         cur = con.cursor()
#         cur.execute("SELECT * FROM Main_rubricks WHERE id=?", (main_rubric_id,))
#         row = cur.fetchall()
#         return row
#
#
#     if mode == 1:
#         maim_rubric_spisok()
#         main_rubric_id = int(input())
#         print('Выбранная вами рубрика:', Selecting_one(main_rubric_id)[0][2])
#
#
#
#     elif mode == 2:
#         Selecting_all()
#         print('Список основных рубрик загружен. Всего: ', len(Selecting_all()), 'основных рубрик')
#
#
#
#     elif mode == 3:
#         maim_rubric_spisok()
#         main_rubric_id = int(input())
#         print('Выбранная вами рубрика:', Selecting_one(main_rubric_id)[0][2])
#
#
#
#     # def get_url(mode):
#     #     print(mode)
#     #
# def window_mode(mode):
#     if mode ==2:
#         start(mode)
#         Selecting_sities(mode)
#         Selecting_main_rubric(mode)
#     elif mode ==1:
#         start(mode)
#         Selecting_main_rubric(mode)
#         Selecting_sities(mode)
#     elif mode ==3:
#         start(mode)
#         Selecting_main_rubric(mode)
#         Selecting_sities(mode)
#     else:
#         restart()

#
# def Parsing_sub_rubric():
#     def make_url_mode_1():
#         for i in Selecting_sities(1):
#             print(i)
#     make_url_mode_1()




def main():
    scene = Scene()


    #
    # Privetstvie()
    # mode = int(input())
    # window_mode(mode)

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






