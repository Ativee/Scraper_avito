
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
        self.btn = Button(root,text='кнопка', command= Child)
        self.btn.pack()


        self.parent_window.mainloop()



class Child(Toplevel):
    def __init__(self):

        self.title('Добавить доходы/расходы')
        self.geometry('400x220+400+300')



def Main():
    root = Tk()
    root.title('Через функцию main')

    main = Parent(root)






if __name__ == '__main__':
    Main()