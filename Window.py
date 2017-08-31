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
        self.a = self.Show_param(('dfd','d','d','d','d','ds'))
        self.root.mainloop()

    def Show_param(self,param):
        z =1
        for i in param:
            z +=1
            self.i = Label(self.root, text=i)
            self.i.grid(row=z)





# class Scene:
#     def __init__(self):
#         self.form = Form()


        #
        # self.form.root.mainloop()



def main():
    scene = Form()



if __name__ == '__main__':
    main()
