import tkinter
import tkinter.messagebox
class Quitter(tkinter.Frame):
    def __init__(self, parent=None):
        tkinter.Frame.__init__(self, parent)
        self.pack()
        widget = tkinter.Button(self, text='Quit', command=self.quit)
        widget.pack(side='left', expand='yes', fill=tkinter.BOTH)
    def quit(self):
        ans = tkinter.messagebox.askokcancel('Verify exit', "Really quit?")
        if ans: tkinter.Frame.quit(self)
if __name__ == '__main__':  Quitter().mainloop()


def main():
    scene = Form()



if __name__ == '__main__':
    main()
