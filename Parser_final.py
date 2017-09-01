
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
        # Кнопка выбора города
        self.sity_list = Button_sity_list_win(self.main_win, self.Open_Sity_list_window,'Выберите необходимые города')
        # Кнопка выбора рубрики
        self.rubric_list = Button_sity_list_win(self.main_win, self.Open_Rubrick_list_window,'Выберите необходимые рубрики')
        self.rubric_list.Sity_list_button.grid(row=3,
                                   column=3,
                                   sticky='e',
                                   padx=5
                                   )


        self.main_win.mainloop()

    def Open_Sity_list_window(self,):

        List_window(self.main_win, 'Отметьте нужные вам города',2)

    def Open_Rubrick_list_window(self):
        List_window(self.main_win, 'Отметьте нужные вам рубрики',1)



    # def Show_param(self,main_win, *param):
    #
    #         # label_par = Label(self.main_win, i)
# class Show_param:
#     def __call__(self, main_win, *param):
#         z = 8
#         for i in param:
#             z += 10
#             self.param_sity_list = Label_info(main_win, i)
#             self.param_sity_list.grid(row=z, columm=5)
#             print('Тестовая кнопка в классе Main_window', i)

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
    def __init__(self,parent, title,param_ex):
        self.Sity_list_win = Toplevel(parent)
        self.Sity_list_win.title(title)
        self.Sity_list_win.geometry('800x600+100+100')

        if param_ex == 1:
            self.project_name = Label_info(self.Sity_list_win,'Отметьте необходимые вам рубрики ')
        elif param_ex == 2:
            self.project_name = Label_info(self.Sity_list_win,'Отметьте необходимые вам города')
        # Создаю список (городов или рубрик)
        self.lis = Listbox(self.Sity_list_win, height=8, width=50,selectmode=MULTIPLE)
        self.list = []
        self.con = lite.connect(str(os.getcwd() + '\GIS.db'))
        self.cur = self.con.cursor()
        if param_ex ==1:
            self.cur.execute("SELECT * FROM Main_rubricks")
            self.row_ind = 1
            for i in self.cur.fetchall():
                self.row_ind += 1
                self.lis.insert(END, i[2])
            self.lis.grid(row=3, column=0, columnspan=2, sticky='w')
            self.sity_list_result = Button(self.Sity_list_win, text='Подтвердите ваш выбор',
                                           command=self.get_selection_rubrick)
            self.sity_list_result.grid(row=4, column=0, sticky='w')

        elif param_ex ==2:
            self.cur.execute("SELECT * FROM Sities_list")
            self.row_ind = 1
            for i in self.cur.fetchall():
                self.row_ind += 1
                self.lis.insert(END, i[0])
            self.lis.grid(row=3, column=0, columnspan=2, sticky='w')

            # создаю кнопку и связываю ее с функцией
            self.sity_list_result = Button(self.Sity_list_win, text='Подтвердите ваш выбор',
                                           command=self.get_selection_sity)
            self.sity_list_result.grid(row=4, column=0, sticky='w')


            # тестовая кнопка
            self.sity_list_result = Button(self.Sity_list_win, text='Тестовая кнопка',
                                           command=(lambda x = self.get_selection_sity(): Show_param(x)))
            self.sity_list_result.grid(row=4, column=1, sticky='w')
        # self.Sity_list_win.focus_set()
        # self.Sity_list_win.grab_set()
        # self.Sity_list_win.wait_window()





    # # Получаем список выденных параметров
    def get_selection_sity(self):
        list_box = self.lis
        self.selection_get = list_box.curselection()
        if len(self.selection_get) == 0:
            print('Вы не выбрали не одного города')
        else:
            print('Выбранные города из списка', self.selection_get,'Всего выбранных городов:', len(self.selection_get))
            Show_param(self.selection_get)

        return (self.selection_get)




    def get_selection_rubrick(self):
        list_box = self.lis
        selection = list_box.curselection()
        if len(selection) == 0:
            print('Вы не выбрали не одной рубрики')
        else:
            print('Выбранные рубрики из списка', selection, 'Всего выбранных рубрик:', len(selection))





















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