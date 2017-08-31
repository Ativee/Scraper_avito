
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

        self.parent_window.mainloop()




def Main():
    root= Tk()
    main = Parent(root)






if __name__ == '__main__':
    Main()