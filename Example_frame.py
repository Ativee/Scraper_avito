from tkinter import *

class Hello(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.data = 42
        self.make_widgets()

    def make_widgets(self):
        widget = Button(self, text='Кнопка', command=self.massage)
        widget.pack

    def massage(self):
        self.data +=1
        print('Выводим в поток значение переменной data %s ' %self.data)

if __name__ == '__main__': Hello().mainloop()
