
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
        # Menushka(self.parent_window)
        self.btn_name = 'Выберите город'
        self.btn = Button(root, text=self.btn_name,
                          command= lambda parent=self.parent_window,name = self.btn_name: (Child(parent,name)))
        self.btn.grid(row=1, column=0)

        self.btn2_name = 'Выберите рубрику'
        self.btn2 = Button(root, text=self.btn2_name,
                          command=lambda parent=self.parent_window, name=self.btn2_name: (Child(parent, name)))
        self.btn2.grid(row=1, column=1)

        # *****
        self.men = Button(root, text=self.btn_name,
                          command=lambda : Menushka(self.parent_window))
        self.men.grid(row=3, column=0)
        # self.sities = get_lis(Child.lis)


        # Выбранные города
        self.Sity = Label(self.parent_window, text='Выбранные города:  ')
        self.Sity.grid(row=2, column=0)
        # Выбранные рубрики
        self.Sity = Label(self.parent_window, text='Выбранные рубрики:  ')
        self.Sity.grid(row=2, column=1)

        self.parent_window.mainloop()

        # Label_1(self.parent_window)
    # def get_lis(self,listi='без параметров'):
    #
    #     self.data_get = listi.curselection()
    #     self.Label_1(self.parent_window, self.data_get)





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

class Child:
    def __init__(self, main_win, name):
        self.parent = main_win
        # self.child = Toplevel(parent)
        # self.child.title(name)
        # self.child.geometry('400x220+400+300')

        self.label = Label(self.parent,text=name)
        self.label.grid(row=1,)
        # Список
        self.lis = Listbox(self.parent, height=8, width=65, selectmode=MULTIPLE)
        for i in Data(name):
            if name == 'Выберите рубрику':
                self.lis.insert(END, i[2])
            elif name == 'Выберите город':
                self.lis.insert(END, i[0])

        self.lis.grid(row=4, sticky='n')

        # Кнопка получить и отправить значения в родительское окно
        self.btn_send = Button(self.parent, text='Подтвердите ваш выбор',
                               # command=lambda listis=self.lis: get_lis(listis)
                               )
        self.btn_send.grid(row=5)

        # self.child.focus_set()
        # self.child.grab_set()
        # self.child.wait_window()


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
    if name == 'Выберите рубрику':
        cur.execute("SELECT * FROM Main_rubricks")
    elif name == 'Выберите город':
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