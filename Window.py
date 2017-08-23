from tkinter import *

root = Tk()

m = Menu(root)  # создается объект Меню на главном окне
root.config(menu=m)  # окно конфигурируется с указанием меню для него

fm = Menu(m)  # создается пункт меню с размещением на основном меню (m)
m.add_cascade(label="File", menu=fm)  # пункту располагается на основном меню (m)
fm.add_command(label="Open...")  # формируется список команд пункта меню
fm.add_command(label="New")
fm.add_command(label="Save...")
fm.add_command(label="Exit")

hm = Menu(m)  # второй пункт меню
m.add_cascade(label="Help", menu=hm)
hm.add_command(label="Help")
hm.add_command(label="About")

root.mainloop()