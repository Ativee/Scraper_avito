import Parsing
from bs4 import BeautifulSoup
import re

from tkinter import *



# def main():
#     # Создание основного окна( функция Тк())
#     root = Tk()
#     root.title('Программа парсинга 2ГИС')
#     root.geometry('1000x500+100+325')
#     # вывод окна на экран
#
#
#     #Создание дочернего окна
#     second = Toplevel(root)
#     second.title('Окно выбора параметров программы')
#     second.geometry('500x250+0+0')
#
#     root.mainloop()
#
class main_window():

    def __init__(self, root):

        self.master = root
        self.master.title('Программа парсинга 2ГИС')
        self.master.geometry('1000x500+100+325')

        c

        self.master.mainloop()

    def child(self):
        def __init__(self):
            self.slave = Toplevel()
            self.slave.title('Параметры парсинга')
            self.slave.geometry('500x200+50+50')



def main():
    root = Tk()

    main_window(root)





#
# def main():
#     # root = Tk()
#     # main_window()
#     root = Tk()
#
#     m = Menu(root)  # создается объект Меню на главном окне
#     root.config(menu=m)  # окно конфигурируется с указанием меню для него
#
#     fm = Menu(m)  # создается пункт меню с размещением на основном меню (m)
#     m.add_cascade(label="File", menu=fm)  # пункту располагается на основном меню (m)
#     fm.add_command(label="Open...")  # формируется список команд пункта меню
#     fm.add_command(label="New")
#     fm.add_command(label="Save...")
#     fm.add_command(label="Exit")
#
#     hm = Menu(m)  # второй пункт меню
#     m.add_cascade(label="Help", menu=hm)
#     hm.add_command(label="Help")
#     hm.add_command(label="About")
#
#     root.mainloop()


if __name__ == '__main__':
    main()