from tkinter import *
class myfun:
    def __init__(self,rootone):
        frame=Frame(rootone)
        frame.pack()
        self.pbutton=Button(frame,text="click",command=self.pmsg)
        self.pbutton.pack()

        self.qbutton=Button(frame,text="exot",command=frame.quit)
        self.qbutton.pack(side=LEFT)


    def pmsg(self):
        print("Clicked")

root=Tk()
obj=myfun(root)
root.mainloop()
