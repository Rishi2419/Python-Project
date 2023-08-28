from tkinter import *
from PIL import ImageTk,Image
from subprocess import call


def go():
    root.destroy()
    call(["Python","backend.py"])
    
root = Tk()
root.geometry("2000x2000")
root.title("Vocabulary Improvement System")

bgimage = ImageTk.PhotoImage(file="xyz.jpg")
bglabel = Label(root,image=bgimage)
bglabel.pack()

title = Label(root,text="VOCABULARY IMPROVEMENT SYSTEM",bg="goldenrod2",font="MicrosoftYaheiUILight 40 bold",fg="firebrick")
title.place(x=275,y=25)

text1 = Label(root,text="* Hey !! I'll help you in improving your vocabulary skills",font="OpenSans 20 bold",fg="firebrick",bd=0,bg="khaki1")
text1.place(x=50,y=170)

text2 = Label(root,text="* Focussing on vocabulary it is useful for developing knowledge\n and skills in multiple aspects of language and literacy",font="OpenSans 20 bold",fg="firebrick",bd=0,bg="khaki1")
text2.place(x=50,y=250)

text3 = Label(root,text="* I'll send you Vocabulary notification which will include a \nnew word followed by its sentence",font="OpenSans 20 bold",fg="firebrick",bd=0,bg="khaki1")
text3.place(x=50,y=370)

text4 = Label(root,text="* You will be getting a new word notification within \nevery 3 hours",font="OpenSans 20 bold",fg="firebrick",bd=0,bg="khaki1")
text4.place(x=50,y=490)

text5 = Label(root,text="* The regular notification will teach you new words regularly",font="OpenSans 20 bold",fg="firebrick",bd=0,bg="khaki1")
text5.place(x=50,y=600)

text6 = Label(root,text="* By clicking on GO button you will start getting notification",font="OpenSans 20 bold",fg="firebrick",bd=0,bg="khaki1")
text6.place(x=50,y=700)

but=Button(root,text="GO",font="OpenSans 40 bold",fg="white",bg="firebrick",bd=0,command=go)
but.place(x=1110,y=400)

root.mainloop()
