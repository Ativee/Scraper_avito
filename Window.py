import Parsing
from bs4 import BeautifulSoup
import re
from tkinter import *
import sqlite3 as lite
import os
import requests
import sys


class Form:
    def __init__(self):
        self.root = Tk()
        self.m = self.root.config()
        self.root.title('Программа парсинга 2ГИС')
        self.root.geometry('800x600+50+50')
        self.width = 50


class Sity_frame_list:
    def __init__(self, form):
        self.k =1
        for i in self.Selecting_sities:
            self.v
            self.k +=1





    def Selecting_sities(self):
        self.list = []
        self.con = lite.connect(str(os.getcwd() + '\GIS.db'))
        self.cur = con.cursor()
        self.cur.execute('SELECT * FROM Sities_list')
        for i in self.cur.fetchall():
            self.list.append(i)
        return self.list

class Scene:
    def __init__(self):
        self.form = Form()
        self.fr = Sity_frame_list(self.form.root)


        self.form.root.mainloop()



def main():
    scene = Scene()



if __name__ == '__main__':
    main()
