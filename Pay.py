from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as mb


root=Tk()


def back():
    root.destroy()
    import Bill








def card():
    root.destroy()
    import cardPay


def cash():
    root.destroy()
    import Cash

root.geometry("850x700")
root.resizable(0,0)

image=Image.open("o.jpg")
ph=ImageTk.PhotoImage(image)
Label(root,image=ph).pack()

image=Image.open("d.jpg")
p=ImageTk.PhotoImage(image)
Label(root,image=p).place(x=70,y=200)
Button(root,text="Pay with card",fg='white',bg='black',font='arial 15 bold',command=card).place(x=110,y=450)



image=Image.open("p.jpg")
m=ImageTk.PhotoImage(image)
Label(root,image=m).place(x=500,y=100)
Button(root,text="Cash",fg='white',bg='black',font='arial 15 bold',command=cash).place(x=550,y=500)



Button(root,text="Back",fg='black',bg='red',font='arial 25 bold',command=back).place(x=330,y=600)


root.mainloop()