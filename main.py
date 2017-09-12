
import os
import sys
from tkinter import *
import re
import requests
import sqlite3 as lite
from bs4 import BeautifulSoup
from selenium import webdriver
import time



class Parent():
    def __init__(self,root, sav_sel_sity=[]):
        self.saved_sity_list = sav_sel_sity
        self.parent_window = root
        self.parent_window.title('Программа парсинга 2Гис')
        self.parent_window.geometry('800x600+50+50')
        # Menushka(self.parent_window)

        # Кнопка открытия выбора списка городов
        self.btn_name = 'Выберите город'
        self.btn = Button(root, text=self.btn_name,
                          command= lambda par=self.parent_window,: Sities_list_box(par))
        self.btn.grid(row=1, column=0)

        # Кнопка открытия выбора списка рубрик
        self.btn2_name = 'Выберите рубрику'
        self.btn2 = Button(root, text=self.btn2_name,
                          command=lambda par=self.parent_window: Rubricks_list_box(par))
        self.btn2.grid(row=1, column=1)
        # *****
        # self.men = Button(root, text=self.btn_name,
        #                   # command=lambda : Menushka(self.parent_window)
        #                   )
        # self.men.grid(row=3, column=0)
        # self.sities = get_lis(Child.lis)


        # Выбранные города

        # Выбранные рубрики

        # Start_parsing(self.parent_window)


        self.parent_window.mainloop()

class Menushka:
    def __init__(self, main_win):
        self.m = Menu(main_win)
        main_win.config(menu=self.m)
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

class Start_parsing:
    def __init__(self,main_win):
        self.btn3 = Button(main_win, text='Произвести парсинг',
                           # command=lambda par=self.parent_window: Rubricks_list_box(par)
                           )
        self.btn3.grid(row=5, column=0)
        s =0
        for i in Parsing_sity:
            s += 1
            param = []
            print(str(s),' Прозведится парсинг города: ' +str(Data('Sity')[i][0]))
            r= 0
            sity_url = Data('Sity')[i][2]
            for rub in Parsing_rubrick:
                r+=1
                time.sleep(1)
                print('Парсинг рубрики: '+str(Data('Rubr')[rub][2]))
                subr_id = Data('Rubr')[rub][0]
                url = str(sity_url + '/' + str(subr_id)+'/?')
                self.url_generate(url)

    def url_generate(self,url):
        response = requests.get(url)
        print('   Страница рубрики для дальнейшей обработки',url)
        print('   ',response.status_code)  # Код ответа
        # print(response.headers)  # Заголовки ответа
        # print(response.text)  # Тело ответа

        # print(url)

        # # soup = BeautifulSoup(response.content)
        # # soup.find_all()


            # print(Data('Sity')[i])



# class Label_Data:
#     def __init__(self,win,list):
#         self.par = win
#         self.row_numb = 5
#         if list is None:
#             pass
#         else:
#             self.row_numb =5
#             for i in list:
#                 self.row_numb +=1
#                 self.label = Label(self.par, text=i)
#                 self.label.grid(row=self.row_numb)

class Sities_list_box:
    def __init__(self, main_win):
        self.par = main_win
        self.lis = Listbox(self.par, height=8, width=65, selectmode=MULTIPLE)

        for i in Data('Sity'):
            self.lis.insert(END, i[0])


        self.lis.grid(row=2,column=0, sticky='n')
        # Кнопка скрыть форму и

        self.btn_send = Button(self.par, text='Подтвердите ваш выбор',
                                command=lambda listis=self.lis: Sities_sel(self.par, listis)
                                )
        self.btn_send.grid(row=3, column=0)


class Rubricks_list_box:
    def __init__(self, main_win):
        self.parent = main_win
        # self.Sity = Label(self.parent, text='Выбранные рубрики:  ')
        # self.Sity.grid(row=2, column=1)
        # Список
        self.lis = Listbox(self.parent, height=8, width=65, selectmode=MULTIPLE)
        for i in Data('Rubr'):
            self.lis.insert(END, i[2])

        self.lis.grid(row=2,column=1, sticky='n')
        # Кнопка скрыть форму
        self.btn_send = Button(self.parent, text='Подтвердите ваш выбор',
                               command=lambda listis=self.lis: Rubrick_sel(self.parent,listis)
                               )
        self.btn_send.grid(row=3,column=1)
#
Parsing_sity =()

class Sities_sel:
    def __init__(self,parent,question):
        self.pa = parent
        self.selecting_sity = question.curselection()
        self.lanel = Label(self.pa, text='Выбрано городов - ' + str(len(self.selecting_sity)))
        self.lanel.grid(row=4,column=0)
        global Parsing_sity
        # print('Предьидущее ',Parsing_sity )
        Parsing_sity = self.selecting_sity
        # print('Последующее ',Parsing_sity )
        if len(Parsing_rubrick) > 0 and len(Parsing_sity)>0:
            Start_parsing(self.pa)


Parsing_rubrick =()

class Rubrick_sel:
    def __init__(self, parent, question):
        self.pa = parent
        self.selecting_rubric = question.curselection()
        self.lanel = Label(self.pa, text='Выбрано рубрик - ' + str(len(self.selecting_rubric)))
        self.lanel.grid(row=4,column=1)
        global Parsing_rubrick
        # print('Предьидущее ', Parsing_rubrick)
        Parsing_rubrick = self.selecting_rubric
        # print('Последующее ', Parsing_rubrick)
        if len(Parsing_sity) > 0 and len(Parsing_rubrick):
            Start_parsing(self.pa)

# class Pars_start():
#     def __init__(self):



# def create_listbox(list):
#     data_get = list.curselection()
#     # new_list = Listbox(Child.parent,height=8, width=65, selectmode=MULTIPLE )
#     # for i in data_get:
#     #     new_list.insert(END, i)
#     # new_list.grid(row=4, sticky='n')
#     print(list)

def Data(name):
    con = lite.connect(str(os.getcwd() + '\GIS.db'))
    cur = con.cursor()
    if name == 'Rubr':
        cur.execute("SELECT * FROM Main_rubricks")
    elif name == 'Sity':
        cur.execute("SELECT * FROM Sities_list")

    data = cur.fetchall()
    return data

# def get_lis(list):
#     data_get = list.curselection()

    print(data_get)


# парсинг
def Pars():
    pass


def Main():
    root = Tk()
    root.title('Через функцию main')
    # print(Parsing_sity)


    main = Parent(root)






if __name__ == '__main__':
    Main()


