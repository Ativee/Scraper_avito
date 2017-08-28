from tkinter import *

# Виджеты
root = Tk() # окно
root.title("Вставка строки")

l_in=Label(root,text="Вставить") # метки
l_num=Label(root,text="Кол-во")
l_pos=Label(root,text="Положение")

e_num=Entry(root, width=5, bg="White") # текстовое поле

pos = IntVar() # радиокнопки
pos.set(0)
r_pos1=Radiobutton(root,text="До", variable=pos, value=0)
r_pos2=Radiobutton(root,text="После", variable=pos, value=1)

b_ok=Button(root,text="OK", width=10) # Кнопки
b_canc=Button(root,text="Отмена", width=10)
b_help=Button(root,text="Справка", width=10)

# Размещение виджетов
l_in.grid(row=0,column=0,columnspan=2,sticky=W,pady=5)
l_num.grid(row=1,column=0)
e_num.grid(row=1,column=1,sticky=W)
l_pos.grid(row=2,column=0,columnspan=2,sticky=W)
r_pos1.grid(row=3,column=0,sticky=W,padx=5)
r_pos2.grid(row=4,column=0,sticky=W,padx=5)
b_ok.grid(row=1,column=2,padx=10,pady=5)
b_canc.grid(row=2,column=2,padx=10,pady=5)
b_help.grid(row=3,column=2,padx=10,pady=5)
#...

root.mainloop()