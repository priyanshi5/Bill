from tkinter import *
import tkinter.messagebox as mb



def sumbit():

    name=e1.get()
    no=e2.get()
    card=e3.get()
    cv=e4.get()
    exp=e5.get()

    if e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="" :
        mb.showerror("Error","Please fill the form")
    if len(card)>12 or len(no)>10:
        mb.showerror("Error","Please enter correct details")
    else:
        mb.showinfo("Success","Payment is Successfull")
        main.destroy()
        import Thank




main=Tk()


main.geometry("600x800")
main.title("card")
main.config(background='yellow')



name=StringVar()
no=StringVar()
card=StringVar()
cv=StringVar()
exp=StringVar()



Label(main,text="Debit Card",font='arial 30 bold',fg='brown').pack()


Label(main,text="Card holder name",font='arial 15 bold',fg='black',bg='yellow').place(x=2,y=100)
e1=Entry(main,width=30,font='arial 15',textvariable=name,bd=7,relief=SUNKEN)
e1.place(x=200,y=100)

Label(main,text="Contact No",font='arial 15 bold',fg='black',bg='yellow').place(x=2,y=200)
e2=Entry(main,width=30,font='arial 15',textvariable=no,bd=7,relief=SUNKEN)
e2.place(x=200,y=200)

Label(main,text="Card No",font='arial 15 bold',fg='black',bg='yellow').place(x=2,y=300)
e3=Entry(main,width=30,font='arial 15',textvariable=card,bd=7,relief=SUNKEN)
e3.place(x=200,y=300)

Label(main,text="CVV",font='arial 15 bold',fg='black',bg='yellow').place(x=2,y=400)
e4=Entry(main,width=30,font='arial 15',textvariable=cv,bd=7,relief=SUNKEN)
e4.place(x=200,y=400)

Label(main,text="Expiry",font='arial 15 bold',fg='black',bg='yellow').place(x=2,y=500)
e5=Entry(main,width=30,font='arial 15',textvariable=exp,bd=7,relief=SUNKEN)
e5.place(x=200,y=500)


Button(main,text="Sumbit",fg='black',bg='red',font='arial 25 bold',command=sumbit).place(x=230,y=600)

main.mainloop()