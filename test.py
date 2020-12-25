from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
# import tkinter.filedialog as fd
howmanytimes=0
howmanytimes_2=0

def testdo(x):
    global howmanytimes
    textbox.delete(0,"end")
    textbox.insert("end",(str(howmanytimes)+"\n"))
    root.after(10,lambda : testdo(x+1))
    howmanytimes=howmanytimes+1
    return 0

def testdo_2(x):
    global howmanytimes_2
    textbox.delete(0,"end")
    textbox_2.insert("end",(str(howmanytimes_2)+"\n"))
    root.after(1000,lambda : testdo_2(x+1))
    howmanytimes_2=howmanytimes_2+1
    return 0

if __name__ == "__main__": 
    root=Tk()
    root.geometry('800x500+350+150')

    # StringVar() 클래스를 testor에 집어넣고 
    testor = StringVar()
    textbox = ttk.Entry(root, width=20,textvariable=testor)
    textbox.grid(column =1, row = 0,padx=20,pady=30)

    textbox_2=Text(root,width=50,height=20)
    textbox_2.grid(column=1,row=2,padx=10,pady=20)

    button_1=ttk.Button(root,text="button_X",command=lambda: [testdo(1),testdo_2(1)],width=20)
    button_1.grid(column=1,row=1)

    menubar=Menu(root)
    filemenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="New",command=lambda: testdo(2))

    root.config(menu=menubar)
    root.mainloop() 