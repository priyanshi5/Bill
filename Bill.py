from tkinter import *

root=Tk()

def exit():
    root.destroy()


def reset():
    name.set("")
    phone.set("")
    order.set("")
    Fries.set("")
    Noodles.set("")
    Burger.set("")
    Pizza.set("")
    Soup.set("")
    Cost.set("")
    Tax.set("")
    Total.set("")
    w.delete(1.0,END)


def price():
    main = Tk()
    main.geometry("300x475+0+0")
    main.resizable(0,0)
    main.config(background="brown")
    main.title("Price List")

    f6=Frame(main,bg='brown',relief=SUNKEN,bd=15)
    f6.pack(side=TOP,fill=X)
    
    Label(f6,text="MENU",bg='brown',fg='black',font='arial 20 bold').pack(fill=Y)

    f7=Frame(main,bg='brown',relief=SUNKEN,bd=15)
    f7.place(x=0,y=85)
    
    Label(f7, font=('aria', 15, 'bold'), text="ITEM", fg="black",bg='brown' ,bd=5).grid(row=0, column=0,padx=20,pady=15)
    
    Label(f7, font=('aria', 15, 'bold'), text="PRICE", fg="black",bg='brown',bd=5).grid(row=0, column=2,padx=20,pady=15)
    
    Label(f7, font=('aria', 15, 'bold'), text="French Fries", fg="yellow",bg='brown').grid(row=1, column=0,padx=20,pady=15)

    Label(f7, font=('aria', 15, 'bold'), text="50", fg="yellow",bg='brown').grid(row=1, column=2,padx=20,pady=15)

    Label(f7, font=('aria', 15, 'bold'), text="Noodles ", fg="yellow",bg='brown').grid(row=2, column=0,padx=20,pady=15)

    Label(f7, font=('aria', 15, 'bold'), text="50", fg="yellow",bg='brown').grid(row=2, column=2,padx=20,pady=15)

    Label(f7, font=('aria', 15, 'bold'), text="Burger ", fg="yellow",bg='brown').grid(row=3, column=0,padx=20,pady=15)

    Label(f7, font=('aria', 15, 'bold'), text="100", fg="yellow",bg='brown').grid(row=3, column=2,padx=20,pady=15)

    Label(f7, font=('aria', 15, 'bold'), text="Pizza ", fg="yellow",bg='brown').grid(row=4, column=0,padx=20,pady=15)

    Label(f7, font=('aria', 15, 'bold'), text="150", fg="yellow",bg='brown').grid(row=4, column=2,padx=20,pady=15)

    Label(f7, font=('aria', 15, 'bold'), text="Soup", fg="yellow",bg='brown').grid(row=5, column=0,padx=20,pady=15)

    Label(f7, font=('aria', 15, 'bold'), text="50", fg="yellow",bg='brown').grid(row=5, column=2,padx=20,pady=15)


    main.mainloop()


def pay():
    root.destroy()
    import Pay





def total():

    f=float(Fries.get()*50)
    n=Noodles.get()*50
    b=Burger.get()*100
    p=Pizza.get()*150
    s=Soup.get()*50

    paycost=float(f + n + b + p + s)

    paytax=float((f + n + b + p + s)*0.08)

    Final=float( paytax + paycost)
    Cost.set(" Rs " +str(paycost))
    Tax.set(" Rs " +str(paytax))
    Total.set(" Rs " +str(Final))

def bill():
    

    f=(Fries.get()*50)
    n=Noodles.get()*50
    b=Burger.get()*100
    p=Pizza.get()*150
    s=Soup.get()*50
    t=0.33
    paycost=float(f + n + b + p + s)

    paytax=float((f + n + b + p + s)*0.086)

    Final=float( paytax + paycost)
       
    w.delete(1.0,END)
    w.insert(END,"\t\t\tWelcome to Goodluck Cafe\n\n\n")
    w.insert(END,f"\n Order No : {order.get()}")
    w.insert(END,f"\n Customer Name : {name.get()}")
    w.insert(END,f"\n Contact No : {phone.get()}")
    w.insert(END,"\n=================================================================")
    w.insert(END,f"\n\nProduct\t\tQuantity\t\tPrice")
    w.insert(END,"\n\n=================================================================\n")
    if (Fries.get()!=0):
        w.insert(END,f"\n French Fries\t\t{Fries.get()}\t\t{f}")
    if (Noodles.get()!=0):
        w.insert(END,f"\n Noodles\t\t{Noodles.get()}\t\t{n}")
    if (Burger.get()!=0):
        w.insert(END,f"\n Burger\t\t{Burger.get()}\t\t{b}")
    if (Pizza.get()!=0):
        w.insert(END,f"\n Pizza\t\t{Pizza.get()}\t\t{p}")
    if (Soup.get()!=0):
        w.insert(END,f"\n Soup\t\t{Soup.get()}\t\t{s}")
    w.insert(END,"\n\n-----------------------------------------------------------------------------------------------------------------------------------")
    w.insert(END,f"\n\nTax\t\t\t{Tax.get()}")
    w.insert(END,"\n\n-----------------------------------------------------------------------------------------------------------------------------------")
    w.insert(END,f"\nTotal Bill : \t\t{Final}")
    w.insert(END,"\n\n-----------------------------------------------------------------------------------------------------------------------------------")
    w.insert(END,f"\n\t\tTHANK YOU.......\n\t\t\tHAVE A GOOD DAY\n")
        

    

root.geometry("1350x900+0+0")
root.title("Billing")
root.config(background='white')
Label(root,text=" GOODLUCK    CAFE ",bg='steelblue',fg='white',bd=12,relief=GROOVE,font='arial 22 bold',pady=20).pack(fill=X)



name=StringVar()
phone=StringVar()
order=StringVar()
Fries = IntVar()
Noodles= IntVar()
Burger=IntVar()
Pizza = IntVar()
Soup=IntVar()
Cost=StringVar()
Tax=StringVar()
Total=StringVar()


f1 = Frame(root,width = 700,height=100,bg='steelblue',relief=GROOVE,bd=12)
f1.pack(side=TOP,fill=X)


Label(f1,text="Customer Name",font='algerian 15 bold',fg='black',bg='steelblue',padx=20,pady=20).grid(row=0,column=0)
e1=Entry(f1,width=15,font='arial 15',textvariable=name,bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

Label(f1,text="Contact No",font='algerian 15 bold',fg='black',bg='steelblue',padx=20,pady=20).grid(row=0,column=2)
e2=Entry(f1,width=15,font='arial 15',textvariable=phone,bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

Label(f1,text="Order no",font='algerian 15 bold',fg='black',bg='steelblue',padx=20,pady=20).grid(row=0,column=4)
e3=Entry(f1,width=15,font='arial 15',textvariable=order,bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

Button(f1,text="Price",width=12,bd=7,bg='black',fg='white',font='arial 15 bold',command=price).grid(row=0,column=7,pady=10,padx=10)





f2=Frame(root,width=350,height=500,bg='steelblue',relief=GROOVE,bd=15)
f2.place(x=5,y=200)



Label(f2,text="Items",font='arial 22 underline bold',fg='maroon',bg='steelblue',bd=10).grid(row=2,column=0)
Label(f2,text="Quantity",font='arial 22 underline bold',fg='maroon',bg='steelblue',bd=10).grid(row=2,column=1)



Label(f2, font=( 'aria' ,16, 'bold' ),text=" French Fries ",fg="blue",bg="steelblue",bd=10).grid(row=3,column=0,padx=10,pady=12)
e4=Entry(f2,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6).grid(row=3,column=1,padx=10,pady=12) 


Label(f2, font=( 'aria' ,16, 'bold' ),text=" Noodles ",fg="blue",bg="steelblue",bd=10).grid(row=4,column=0,padx=10,pady=12)
e5= Entry(f2,font=('ariel' ,16,'bold'), textvariable=Noodles , bd=6).grid(row=4,column=1,padx=10,pady=12)


Label(f2, font=( 'aria' ,16, 'bold' ),text="Burger ",fg="blue",bg="steelblue",bd=10).grid(row=5,column=0,padx=10,pady=12)
e6=Entry(f2,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6).grid(row=5,column=1,padx=10,pady=12)

Label(f2, font=( 'aria' ,16, 'bold' ),text="Pizza ",fg="blue",bg="steelblue",bd=10).grid(row=6,column=0,padx=10,pady=12)
e7=Entry(f2,font=('ariel' ,16,'bold'), textvariable=Pizza , bd=6).grid(row=6,column=1,padx=10,pady=12)


Label(f2, font=( 'aria' ,16, 'bold' ),text="Soup",fg="blue",bg="steelblue",bd=10).grid(row=7,column=0,padx=10,pady=12)
e8=Entry(f2,font=('ariel' ,16,'bold'), textvariable=Soup , bd=6).grid(row=7,column=1,padx=10,pady=12)






f3=Frame(root,width=500,height=1000,bd=15,relief=GROOVE,bg='steelblue')
f3.place(x=500,y=200)

#Label(f3,text="Bill",font='arial 25 underline',fg='red',bg='pink',bd=10).grid(row=2,column=3)

Label(f3, font=( 'aria' ,16, 'bold' ),text="Cost",fg="black",bd=10,bg='steelblue').grid(row=4,column=2,padx=20,pady=45)
e9=Entry(f3,font=('ariel' ,16,'bold'), textvariable=Cost , bd=6,bg="white").grid(row=4,column=3,padx=20,pady=45)

Label(f3, font=( 'aria' ,16, 'bold' ),text="Tax",fg="black",bd=10,bg='steelblue').grid(row=6,column=2,padx=20,pady=45)
e10=Entry(f3,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,bg="white").grid(row=6,column=3,padx=20,pady=45)

Label(f3, font=( 'aria' ,16, 'bold' ),text="Total",fg="gold",bd=10,bg='steelblue').grid(row=8,column=2,padx=20,pady=45)
e11=Entry(f3,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,bg="grey").grid(row=8,column=3,padx=20,pady=45)

#Button(f3,text="Confirm",width=12,bd=7,font='arial 16 bold',bg='red',fg='black',command=chk).grid(row=10,column=3,padx=10,pady=20)


f4=Frame(root,width=300,height=440,bd=15,relief=GROOVE,bg='steelblue')
f4.place(x=950,y=200)

Label(f4,text="Bill",font='arial 16 bold',fg='black',bg='steelblue',bd=10).pack(fill=X)

scroll=Scrollbar(f4,orient=VERTICAL)
w=Text(f4,yscrollcommand=scroll.set,width=75,bg='white',font='arial 10')
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=w.yview,bg='white')
w.pack()



f5=Frame(root,width=50,height=120,bd=12,relief=GROOVE,bg='steel blue')
f5.pack(side=BOTTOM,fill=X)

Button(f5,text="Total",width=12,bd=7,font='arial 16 bold',bg='red',fg='black',command=total).grid(row=10,column=2,pady=40,padx=27)

Button(f5,text="Reset",width=12,bd=7,font='arial 16 bold',bg='red',fg='black',command=reset).grid(row=10,column=4,pady=40,padx=27)

Button(f5,text="Exit",width=12,bd=7,font='arial 16 bold',bg='red',fg='black',command=exit).grid(row=10,column=6,pady=40,padx=27)

Button(f5,text="Bill",width=12,bd=7,font='arial 16 bold',bg='red',fg='black',command=bill).grid(row=10,column=8,pady=40,padx=27)

Button (f5,text="Pay",width=12,bd=7,font='arial 16 bold',bg='red',fg='black',command=pay).grid(row=10,column=10,pady=40,padx=27)




root.mainloop()