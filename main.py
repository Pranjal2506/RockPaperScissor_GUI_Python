from tkinter import *
from PIL import ImageTk, Image
import random


user=0
comp=0

def reset():
    global user,comp,u_text,c_text
    user=0
    comp=0
    u_text=(f"User:- {user}")
    c_text=(f"Computer:- {comp}")
    p_score.config(text=u_text)
    c_score.config(text=c_text)
    result.config(text="")
    
def rock():
    global user,comp,u_text,c_text
    shuffel()
    if opponent == "Rimg_":
        result.config(text="DRAW")
    elif opponent == "Simg_":
        result.config(text="YOU WIN")
        user = user+1
        u_text=(f"User:- {user}")
        p_score.config(text=u_text)
    else:
        comp = comp + 1
        c_text=(f"Computer:- {comp}")
        c_score.config(text=c_text)
        result.config(text="YOU LOOSE")
    return 0
def paper():
    global user,comp,u_text,c_text
    shuffel()
    if opponent == "Pimg_":
        result.config(text="DRAW")
    elif opponent == "Rimg_":
        result.config(text="YOU WIN")
        user = user+1
        u_text=(f"User:- {user}")
        p_score.config(text=u_text)
    else:
        comp = comp + 1
        c_text=(f"Computer:- {comp}")
        c_score.config(text=c_text)
        result.config(text="YOU LOOSE")
    return 0
def scissor():
    global user,comp,u_text,c_text
    shuffel()
    if opponent == "Simg_":
        result.config(text="DRAW")
    elif opponent == "Pimg_":
        result.config(text="YOU WIN")
        user = user+1
        u_text=(f"User:- {user}")
        p_score.config(text=u_text)
    else:
        comp = comp + 1
        c_text=(f"Computer:- {comp}")
        c_score.config(text=c_text)
        result.config(text="YOU LOOSE")
    return 0


def shuffel():
    global opponent
    lst_img=["Rimg_","Pimg_","Simg_"]
    final=random.choice(lst_img)
    opp_turn.config(image=eval(final))
    opp_turn.config(text=final)
    opponent=opp_turn.cget('text')
    return 0
    
font=("Comic Sans Ms",15,'bold')
win=Tk()
win.geometry("400x490")
win.config(bg="lightblue")
win.title("Rock Paper Scissor")

img1=Image.open("rock.png").resize((100,100))
img_1=Image.open("rock_.png").resize((100,100))
Rimg=ImageTk.PhotoImage(img1)
Rimg_=ImageTk.PhotoImage(img_1)
rock=Button(win,image=Rimg,text="rock",borderwidth=0,bg="lightblue",activebackground="lightblue",command=rock)
rock.place(x=10,y=10)

img2=Image.open("paper.png").resize((100,100))
img_2=Image.open("paper_.png").resize((100,100))
Pimg=ImageTk.PhotoImage(img2)
Pimg_=ImageTk.PhotoImage(img_2)
paper=Button(win,image=Pimg,text="paper",borderwidth=0,bg="lightblue",activebackground="lightblue",command=paper)
paper.place(x=10,y=160)

img3=Image.open("scissors.png").resize((100,100))
img_3=Image.open("scissors_.png").resize((100,100))
Simg=ImageTk.PhotoImage(img3)
Simg_=ImageTk.PhotoImage(img_3)
scissor=Button(win,image=Simg,text="scissor",borderwidth=0,bg="lightblue",activebackground="lightblue",command=scissor)
scissor.place(x=10,y=320)

result=Label(win,text="",font=font,bg="lightblue")
result.place(x=15_3,y=200)
opp_turn=Label(win,image=None,bg="lightblue",text="")
opp_turn.pack(side=RIGHT)

p_score=Label(win,text="User:- 0",font=font,bg="lightblue")
p_score.place(x=20,y=410)
c_score=Label(win,text="Computer:- 0",font=font,bg="lightblue")
c_score.place(x=260,y=410)

reset=Button(win,text="Reset",font=("Comic Sans Ms",12,'bold'),relief=RAISED, background="lightgreen",command=reset)
reset.place(x=170,y=410)

info=Label(win,text="Developed by Pranjal Raghuvanshi.",font=("Comic Sans Ms",12,'bold'),bg="lightblue")
info.place(x=60,y=460)

win.iconphoto(False,Pimg)
win.mainloop()