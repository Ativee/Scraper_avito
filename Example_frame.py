from tkinter import *                          # get widget classes
from tkinter.messagebox import askokcancel     # get canned std dialog

class Quitter1(Button):                          # subclass our GUI
    def __init__(self, master):           # constructor method
        Button.__init__(self, master)
        widget = Button(master, text='Quit', command=self.quit1)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)
        self.P = master

    def quit1(self):
        ans = askokcancel('Verify exit', "Really quit?")
        if ans:
            self.P.quit()
            self.P.destroy()

if __name__ == '__main__':
    root = Tk()
    Q = Quitter1(root)
    Q.mainloop()