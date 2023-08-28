from tkinter import *
from PIL import ImageTk
from subprocess import call
from tkinter import messagebox
import pymysql

def signupbutton():
      root.destroy()
      call(["Python","signup.py"])

def user_enter(event):
    if usernameEntry.get()=="Username":
          usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=="Password":
          passwordEntry.delete(0,END)

def hide():
     openeye.config(file="closeye.png")
     passwordEntry.config(show="*")
     eyebutton.config(command=show)

def show():
          openeye.config(file="openeye.png")
          passwordEntry.config(show="")
          eyebutton.config(command=hide)

def login_user():
      if usernameEntry.get()=="" or passwordEntry.get()=="":
            messagebox.showerror("Error","All Fields Are Required")
      else:
            try:
                  con=pymysql.connect(host="localhost",user="root",password="1908")
                  mycursor=con.cursor()
            except:
                  messagebox.showerror("Error","Connection is not established try again")
                  return
            query = "use userdata"
            mycursor.execute(query)
            query="select * from data where username=%s and password=%s"
            mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
            row=mycursor.fetchone()
            if row == None:
                  messagebox.showerror("Error","Invalid Username or Password")
            else:
                  root.destroy()
                  call(["Python","gui.py"])


root=Tk()
root.geometry("990x660+50+50")
root.resizable(0,0)
root.title("Login Page")

bgimage = ImageTk.PhotoImage(file="bg.jpg")
bglabel = Label(root,image=bgimage)
bglabel.place(x=0,y=0)

heading=Label(root,text="USER LOGIN",font= "MicrosoftYaheiUILight 23 bold",bg="white",fg="firebrick")
heading.place(x=605,y=120)

usernameEntry=Entry(root,font= "MicrosoftYaheiUILight 11 bold",bd=0,bg="white",fg="firebrick")
usernameEntry.place(x=580,y=200)

usernameEntry.insert(0,"Username")
usernameEntry.bind("<FocusIn>",user_enter)

frame1=Frame(root,width=250,height=2,bg="firebrick")
frame1.place(x=580,y=222)

passwordEntry=Entry(root,font= "MicrosoftYaheiUILight 11 bold",bd=0,bg="white",fg="firebrick")
passwordEntry.place(x=580,y=260)

passwordEntry.insert(0,"Password")
passwordEntry.bind("<FocusIn>",password_enter)

frame2=Frame(root,width=250,height=2,bg="firebrick")
frame2.place(x=580,y=282)

openeye=PhotoImage(file="openeye.png")
eyebutton= Button(root,image=openeye,bd=0,bg="white",activebackground="white",cursor="hand2",command=hide)
eyebutton.place(x=800,y=255)

loginwindow=Button(root,text="Login",font="OpenSans 16 bold",fg="white",bg="firebrick",cursor="hand2",bd=0,width=19,command=login_user)
loginwindow.place(x=578,y=350)

orlabel=Label(root,text="---------------OR--------------",font="OpenSans 16 ",bg="white",fg="firebrick")
orlabel.place(x=583,y=400)

facebook_logo=PhotoImage(file="facebook.png")
facebook=Label(root,image=facebook_logo,bg="white")
facebook.place(x=640,y=440)

google_logo=PhotoImage(file="google.png")
google=Label(root,image=google_logo,bg="white")
google.place(x=740,y=440)

signup=Label(root,text="Dont have an account?",font= "OpenSans 9 bold",fg= "firebrick",bg="white")
signup.place(x=590,y=500)

newaccbutton=Button(root,text="Create new  Account",font="OpenSans 9 underline",fg="blue",bg="white",cursor="hand2",bd=0,command=signupbutton)
newaccbutton.place(x=727,y=500)
root.mainloop()