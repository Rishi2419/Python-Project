from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
from subprocess import call
import pymysql

def clear():
    emailentry.delete(0,END)
    userentry.delete(0,END)
    passwordentry.delete(0,END)
    confirmentry.delete(0,END)
    check.set(0) 

def connect_database():
    if emailentry.get()=="" or userentry.get()=="" or passwordentry.get()=="" or confirmentry.get()=="" :
        messagebox.showerror("Error","All fields are required")
    elif passwordentry.get() != confirmentry.get() :
        messagebox.showerror("Error","Password Mismatch")   
    elif check.get()==0:
        messagebox.showerror("Error","Please Accept Terms and Conditions")
    else:
        try:
         con=pymysql.connect(host="localhost",user="root",password="1908")
         mycursor=con.cursor()
        except:
            messagebox.showerror("Error","Database Connectivity Issue,Please Try Again")
    try:
        query="create database userdata"
        mycursor.execute(query)
        query="use userdata"
        mycursor.execute(query)

        query="create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))"
        mycursor.execute(query)
    except:
        mycursor.execute("use userdata")

    query="select * from data where username =%s"
    mycursor.execute(query,(userentry.get()))

    row=mycursor.fetchone()
    if row != None:
        messagebox.showerror("Error","Username Already Exists" )
    else:
        query="insert into data(email,username,password) values(%s,%s,%s)"
        mycursor.execute(query,(emailentry.get(),userentry.get(),passwordentry.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Sucsess",     "Registration is Successful")

        clear()
        root.destroy()
        call(["Python","login.py"])




def close():
    root.destroy()
    call(["Python","login.py"])

root = Tk()
root.geometry("990x660+50+50")
root.resizable(0,0)
root.title("Signup")

bgimage = ImageTk.PhotoImage(file="bg.jpg")
bglabel = Label(root,image=bgimage)
bglabel.grid()

frame1= Frame(root,bg="white")
frame1.place(x=554,y=100)
heading=Label(frame1,text="CREATE AN ACCOUNT",font= "MicrosoftYaheiUILight 18 bold",bg="white",fg="firebrick1")
heading.grid(row=0,column=0,padx=10,pady=10)

email= Label(frame1,text="Email",font= "MicrosoftYaheiUILight 10 bold",bg="white",fg="firebrick1")
email.grid(row=1,column=0,sticky="w",padx=25,pady=(15,0))
emailentry= Entry(frame1,width=30, font= "MicrosoftYaheiUILight 10 bold",fg="white",bg="firebrick1")
emailentry.grid(row=2,column=0,sticky="w",padx=25)

username= Label(frame1,text="Username",font= "MicrosoftYaheiUILight 10 bold",bg="white",fg="firebrick1")
username.grid(row=3,column=0,sticky="w",padx=25,pady=(15,0))
userentry= Entry(frame1,width=30, font= "MicrosoftYaheiUILight 10 bold",fg="white",bg="firebrick1")
userentry.grid(row=4,column=0,sticky="w",padx=25)

password= Label(frame1,text="Password",font= "MicrosoftYaheiUILight 10 bold",bg="white",fg="firebrick1")
password.grid(row=5,column=0,sticky="w",padx=25,pady=(15,0))
passwordentry= Entry(frame1,width=30, font= "MicrosoftYaheiUILight 10 bold",fg="white",bg="firebrick1")
passwordentry.grid(row=6,column=0,sticky="w",padx=25)

confirm= Label(frame1,text="Confirm Password",font= "MicrosoftYaheiUILight 10 bold",bg="white",fg="firebrick1")
confirm.grid(row=7,column=0,sticky="w",padx=25,pady=(15,0))
confirmentry= Entry(frame1,width=30, font= "MicrosoftYaheiUILight 10 bold",fg="white",bg="firebrick1")
confirmentry.grid(row=8,column=0,sticky="w",padx=25)
check= IntVar()
termsandchkcondition= Checkbutton(frame1,text="I agree to the Terms and the Condition",font= "MicrosoftYaheiUILight 10 bold",bg="white",fg="firebrick1",cursor="hand2",variable=check)
termsandchkcondition.grid(row=9,column=0,padx=10,pady=25)

signupbutton=Button(frame1,text="Signup",width=20,font="OpenSans 16 bold",fg="white",bg="firebrick",cursor="hand2",command=connect_database)
signupbutton.grid(row=10,column=0)

alreadyacc=Label(frame1,text= "Already have an account?",font="OpenSans 9 bold",bg="white",fg="firebrick1")
alreadyacc.grid(row=11,column=0,sticky="w",padx=25,pady=10)

loginbutton=Button(frame1,text="Log in",font="OpenSans 9 underline",fg="blue",bg="white",cursor="hand2",bd=0,command=close)
loginbutton.place(x=190,y=410)

root.mainloop()