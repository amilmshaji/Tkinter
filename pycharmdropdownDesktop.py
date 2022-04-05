from tkinter import *
root=Tk()

def fun1():
    print("creating new project")
def fun2():
    print("creating new file")
def fun3():
    print("creating new scratch file")
def fun4():
    print("open files")
def fun5():
    print("saving files")
mymenu=Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)

mymenu.add_cascade(label="file",menu=submenu)
submenu.add_command(label="New project",command=fun1)
submenu.add_command(label="New",command=fun2)
submenu.add_separator()
submenu.add_command(label="New scratch file",command=fun3)
submenu.add_command(label="open",command=fun4)
submenu.add_separator()
submenu.add_command(label="Save",command=fun4)
submenu.add_command(label="Exit",command=quit)

newmenu1=Menu(mymenu)
mymenu.add_cascade(label="edit",menu=newmenu1)
newmenu1.add_command(label="undo")
newmenu1.add_command(label="redo")
newmenu1.add_separator()
newmenu1.add_command(label="cut")
newmenu1.add_command(label="copy")
newmenu1.add_separator()
newmenu1.add_command(label="paste")
newmenu1.add_command(label="delete")

newmenu2=Menu(mymenu)
mymenu.add_cascade(label="view",menu=newmenu2)
newmenu2.add_command(label="Tool Windows")
newmenu2.add_command(label="apperance")
newmenu2.add_separator()
newmenu2.add_command(label="Recent files")
newmenu2.add_command(label="recent change files")
newmenu2.add_separator()
newmenu2.add_command(label="horizontal")
newmenu2.add_command(label="vertical")

newmenu3=Menu(mymenu)
mymenu.add_cascade(label="code",menu=newmenu3)
newmenu3.add_command(label="Review")
newmenu3.add_command(label="inspect")
newmenu3.add_separator()
newmenu3.add_command(label="unwrap")
newmenu3.add_command(label="analze")
newmenu3.add_separator()
newmenu3.add_command(label="move upline")
newmenu3.add_command(label="move downline")

newmenu4=Menu(mymenu)
mymenu.add_cascade(label="Run",menu=newmenu4)
newmenu4.add_command(label="Run")
newmenu4.add_command(label="Debug")
newmenu4.add_separator()
newmenu4.add_command(label="toggle")
newmenu4.add_command(label="import")
newmenu4.add_separator()
newmenu4.add_command(label="export")
newmenu4.add_command(label="exit")


root.mainloop()