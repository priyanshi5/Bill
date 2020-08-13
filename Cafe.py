from tkinter import *
import tkinter.messagebox as mb
import mysql.connector
main=Tk()

def chk():
    conn=mysql.connector.connect(host='localhost',user="root",password="",db="Rest")
    cr=conn.cursor()
    user=e1.get()
    pwd=e2.get()
    cr.execute("select * from login where usr='"+user+"' and pwd='"+pwd+"'")
    if(cr.fetchone()):
        main.destroy()
        import Bill
    else:
        mb.showinfo("Error","Data Not Match")
    #e1.delete(0,END)
    #e2.delete(0,END)
    #e1.focus()

    
main.config(background="cyan")
main.title("Login Window")
main.geometry("1010x504+100+100")
main.resizable(0,0)
photo=PhotoImage(file="Restaurant.png")
Label(main,image=photo,padx=10,pady=70).place(x=0,y=0)

Label(main,text="User ID",fg="red",relief=RIDGE,bd=15,bg="white",font=("Arial",22,'bold')).place(x=200,y=150)
Label(main,text="Password",fg="red",relief=RIDGE,bd=15,bg="white",font=("Arial",22,'bold')).place(x=200,y=250)

e1=Entry(main,width=15,relief=RIDGE,bd=15,font='arial 16 bold')
e1.place(x=400,y=150)
e2=Entry(main,show='*',width=15,relief=RIDGE,bd=15,font='arial 16 bold')
e2.place(x=400,y=250)
Button(main,text="Signin",width=15,relief=RIDGE,bd=15,font='arial 16 bold',bg='steelblue',command=chk).place(x=250,y=400)
Button(main,text="Cancel",width=15,relief=RIDGE,bd=15,font='arial 16 bold',bg='steelblue').place(x=600,y=400)
main.mainloop()