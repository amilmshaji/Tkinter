from tkinter import *
root=Tk()

def fun1():
    print("Hai click")

mymenu=Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)

mymenu.add_cascade(label="file",menu=submenu)
submenu.add_command(label="save")
submenu.add_command(label="save as")
submenu.add_separator()
submenu.add_command(label="save")
submenu.add_command(label="save")


newmenu=Menu(mymenu)
mymenu.add_cascade(label="edit",menu=newmenu)
newmenu.add_command(label="undo",command=fun1)
root.mainloop()