from tkinter import *
from subprocess import call

from PIL import ImageTk,Image
def program ():
    root.destroy()
    call(["Python","main.py"])

root = Tk()
root.geometry("2000x2000")
# root.resizable(0,0)
# root.geometry("700x700")
# root.minsize(300,300)
#root.maxsize(900,1000)
root.title("Vocabulary Improvement System")

bg=Label(root,bg="CadetBlue3",width=2000,height=2000)
bg.place(x=0,y=0)

bgimage = ImageTk.PhotoImage(file="xyz.png")
bglabel = Label(root,image=bgimage,bd=0)
bglabel.pack()

text=Label(root,text="SO START YOUR JOURNEY WITH ME AND LEARN SOME NEW WORDS",font="MicrosoftYaheiUILight 30 bold",bg="blue4",fg="white")
text.place(x=100,y=760)

Button = Button(root,text="START",font="MicrosoftYaheiUILight 40 bold",fg="white",bg="firebrick",cursor="hand2",bd=0,command=program)
Button.place(x=1200,y=500)



root.mainloop()
