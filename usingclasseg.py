from tkinter import *
class student:
        def __init__(self,rootone):
            frame=Frame(rootone).pack()
            self.label=Label(frame,text="Student Detail").pack()
            self.button1=Button(frame,text="view",command=self.pmsg1).pack()
            self.button2=Button(frame,text="Cancel",command=self.pmsg2).pack()
            self.button3=Button(frame,text="exit",command=quit)
            self.button3.pack()
        def pmsg1(self):
            print("click them")
        def pmsg2(self):
            print("cancelled")
root=Tk()
obj=student(root)
root.mainloop()