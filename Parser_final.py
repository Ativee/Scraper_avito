
import os
import sys
from tkinter import *
import re
import requests
import sqlite3 as lite
from bs4 import BeautifulSoup


class Main_window():
    def __init__(self,main_win):
        self.main_win = main_win
        self.main_win.title('Программа парсинга 2ГИС')
        self.main_win.geometry('800x600+50+50')
        self.main_win.config()
        Menushka(self.main_win)
        self.sity_list = Button_sity_list_win(self.main_win, self.Open_Sity_list_window,'Выберите необходимые города')

        self.rubric_list = Button_sity_list_win(self.main_win, self.Open_Rubrick_list_window,'Выберите необходимые рубрики')
        self.rubric_list.Sity_list_button.grid(row=3,
                                   column=3,
                                   sticky='e',
                                   padx=5
                                   )

        self.main_win.mainloop()



    def Open_Sity_list_window(self):
        List_window(self.main_win, 'Отметьте нужные вам города')

    def Open_Rubrick_list_window(self):
        List_window(self.main_win, 'Отметьте нужные вам рубрики')



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



class List_window():
    def __init__(self,parent, title):

        self.Sity_list_win = Toplevel(parent)
        self.Sity_list_win.title(title)
        self.Sity_list_win.geometry('800x600+100+100')
        self.project_name =Label_info(self.Sity_list_win, 'Выберите нужные вам города, при необходимости можно выбрать')
        #
        self.lis = Listbox(self.Sity_list_win, height=8, width=20,selectmode=MULTIPLE)

        self.list = []
        self.con = lite.connect(str(os.getcwd() + '\GIS.db'))
        self.cur = self.con.cursor()
        self.cur.execute('SELECT * FROM Sities_list')
        self.row_ind = 1
        for i in self.cur.fetchall():
            self.row_ind += 1
            self.lis.insert(END, i[0])
        self.lis.grid(row=3 , column=0, columnspan=2)



        #     self.ss = Label(self.Sity_list_win,text=i).grid(row=2 + self.row_ind, column=1)
        #
        #
        #
        # self.Sity_list_win.grab_set()
        # self.Sity_list_win.focus_set()
        # self.Sity_list_win.wait_window()





    # def DB_sity_list(self,parent):






class Button_sity_list_win():
    def __init__(self,parent,func,text):

        self.Sity_list_button = Button(parent,
                                       text=text,
                                       command=func
                                       )
        self.Sity_list_button.grid(row=3,
                                   column=2,
                                   sticky='e',
                                   padx=5
                                   )

class Label_info():
    def __init__(self,parent,question):
        self.name = Label(parent,text=question)
        self.name.grid(row=1,column=1)




class Program():
    def __init__(self):
        self.main_win = Tk()
        self.window = Main_window(self.main_win)



def main():

    Program()



if __name__ == '__main__':
    main()