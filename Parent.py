
import os
import sys
from tkinter import *
import re
import requests
import sqlite3 as lite
from bs4 import BeautifulSoup



class Parent():
    def __init__(self,root):
        self.parent_window = root
        self.parent_window.title('Программа парсинга 2Гис')
        self.parent_window.geometry('800x600+50+50')
        Menushka(self.parent_window)

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
        # self.Sity = Label(self.par, text='Выбранные города:  ')
        # self.Sity.grid(row=2, column=0)
        # Список
        self.lis = Listbox(self.par, height=8, width=65, selectmode=MULTIPLE)

        for i in Data('Sity'):
            self.lis.insert(END, i[0])


        self.lis.grid(row=2,column=0, sticky='n')
        # Кнопка скрыть форму и
        self.btn_send = Button(self.par, text='Подтвердите ваш выбор',
                               command=lambda listis=self.lis: Sities_sel(self.par,listis)
                               )
        self.btn_send.grid(row=3,column=0)

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
class Sities_sel:
    def __init__(self,parent,question):
        self.pa = parent
        self.slave = Toplevel(self.pa)
        self.sel = question.curselection()

        self.slave.title('child')
        self.slave.geometry('200x150+500+375')
        self.lanel = Label(self.slave, text='Всего выбрано: '+str(len(self.sel))+' городов')
        self.lanel.grid()
        for i in self.sel:
            print(Data('Sity')[i][0])
            self.lanel_sel = Label(self.slave, text=str(Data('Sity')[i][0]))
            self.lanel_sel.grid()


        self.slave.grab_set()
        self.slave.focus_set()
        self.slave.wait_window()




class Rubrick_sel:
    def __init__(self, parent, question):
        self.pa = parent
        self.slave = Toplevel(self.pa)
        self.sel = question.curselection()

        self.slave.title('child')
        self.slave.geometry('300x150+500+375')
        self.lanel = Label(self.slave, text='Всего выбрано: ' + str(len(self.sel)) + ' рубрик')
        self.lanel.grid()
        for i in self.sel:
            # print(Data('Rubr')[i][2])
            self.lanel_sel = Label(self.slave, text=str(Data('Rubr')[i][2]))
            self.lanel_sel.grid()

        self.slave.grab_set()
        self.slave.focus_set()
        self.slave.wait_window()


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




def Main():
    root = Tk()
    root.title('Через функцию main')


    main = Parent(root)






if __name__ == '__main__':
    Main()


