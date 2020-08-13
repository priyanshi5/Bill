from tkinter import *
from PIL import ImageTk,Image

main=Tk()
main.geometry("800x600")
main.resizable(0,0)
image=Image.open("thank.jpg")
p=ImageTk.PhotoImage(image)
Label(main,image=p).pack()

main.mainloop()
