
from tkinter import Tk,ttk,Button
from tkinter import messagebox
from random import randint
import sys
#getting the active player
ActivePlayer = 1
#allow the users to chose a name before game begines.
d1 = input('player {1} enter your name ')
d2= input('player {2} enter your name ')
#this is the code for directing to the terminal
print("xxxxxx  xxxxx   xxxxxxxx     xxx       xxx   xx   xx      xx      xx      xx       ")
print("  xx    xx      x     xx     xx  x   x  xx   xx   xx x    xx    xx  xx    xx       ")
print("  xx    xxxxx   xx  xx       xx    x    xx   xx   xx   x  xx   xx xx xx   xx       ")
print("  xx    xx      xx    xx     xx         xx   xx   xx    x xx  xx      xx  xx       ")
print("  xx    xxxxx   xx     xx    xx         xx   xx   xx      xx xx        xx xxxxxxxx ")
print('***proceed to the terminal to continue playing.***')

#declaring player {1} and {2}

p1 = []
p2 = []
mov = 0

def SetLayout(id,player_symbol):
    if id==1:
        b1.config(text= player_symbol)
        b1.state(['disabled'])
    elif id==2:
        b2.config(text= player_symbol)
        b2.state(['disabled'])
    elif id==3:
        b3.config(text= player_symbol)
        b3.state(['disabled'])
    elif id==4:
        b4.config(text= player_symbol)
        b4.state(['disabled'])
    elif id==5:
        b5.config(text= player_symbol)
        b5.state(['disabled'])
    elif id==6:
        b6.config(text= player_symbol)
        b6.state(['disabled'])
    elif id==7:
        b7.config(text= player_symbol)
        b7.state(['disabled'])
    elif id==8:
        b8.config(text= player_symbol)
        b8.state(['disabled'])
    elif id==9:
        b9.config(text= player_symbol)
        b9.state(['disabled'])

def lookup_winner():
    global mov
    winner = -1

    if(1 in p1) and (2 in p1) and (3 in p1):
        winner = 1
    if(1 in p2) and (2 in p2) and (3 in p2):
        winner = 2

    if(4 in p1) and (5 in p1) and (6 in p1):
        winner = 1
    if(4 in p2) and (5 in p2) and (6 in p2):
        winner = 2

    if(7 in p1) and (8 in p1) and (9 in p1):
        winner = 1
    if(7 in p2) and (8 in p2) and (9 in p2):
        winner = 2

    if(1 in p1) and (4 in p1) and (7 in p1):
        winner = 1
    if(1 in p2) and (4 in p2) and (7 in p2):
        winner = 2

    if(2 in p1) and (5 in p1) and (8 in p1):
        winner = 1
    if(2 in p2) and (5 in p2) and (8 in p2):
        winner = 2

    if(3 in p1) and (6 in p1) and ( 9 in p1):
        winner = 1
    if(3 in p2) and (6 in p2) and (9 in p2):
        winner = 2

    if(1 in p1) and (5 in p1) and ( 9 in p1):
        winner = 1
    if(1 in p2) and (5 in p2) and (9 in p2):
        winner = 2

    if(3 in p1) and (5 in p1) and ( 7 in p1):
        winner = 1
    if(3 in p2) and (5 in p2) and (7 in p2):
        winner = 2

    if winner ==1:
        messagebox.showinfo(title="you win!!!.",
            message= d1+ " is the winner")
        Restart()
    elif winner ==2:
        messagebox.showinfo(title="you win!!!.",
            message= d2+ " is the winner")
        Restart()

    elif mov ==9:
        messagebox.showinfo(title="Draw",
            message="Draw-Draw!!")
        Restart()

def ButtonClick(id):
    global ActivePlayer
    global p1, p2
    global mov

    if(ActivePlayer ==1):
        SetLayout(id,"X")
        p1.append(id)
        mov +=1
        root.title("XnO : "+d2)
        ActivePlayer =2

    elif(ActivePlayer==2):
        SetLayout(id,"O")
        p2.append(id)
        mov +=1
        root.title("XnO : "+d1)
        ActivePlayer =1
    lookup_winner()

def AutoPlay():
    global p1; global p2
    Empty = []
    for cell in range(9):
        if(not((cell +1 in p1) or (cell +1 in p2))):
            Empty.append(cell+1)
    try:
        RandIndex = randint(0,len(Empty) -1)
        ButtonClick(Empty[RandIndex])
    except:
        pass

def EnableAll():
    b1.config(text= " ")
    b1.state(['!disabled'])
    b2.config(text= " ")
    b2.state(['!disabled'])
    b3.config(text= " ")
    b3.state(['!disabled'])
    b4.config(text= " ")
    b4.state(['!disabled'])
    b5.config(text= " ")
    b5.state(['!disabled'])
    b6.config(text= " ")
    b6.state(['!disabled'])
    b7.config(text= " ")
    b7.state(['!disabled'])
    b8.config(text= " ")
    b8.state(['!disabled'])
    b9.config(text= " ")
    b9.state(['!disabled'])


def Restart():
    global p1,p2,mov,ActivePlayer
    p1.clear(); p2.clear()
    mov,ActivePlayer = 0,1
    root.title("XnO : Player 1")
    EnableAll()




root = Tk()
root.title("XnO : "+d1)
st = ttk.Style()
st.configure("my.TButton", font=('Chiller',24,'bold'))

b1 = ttk.Button(root, text=".. ", style="my.TButton")
b1.grid(row=1, column=0, sticky="nwse", ipadx=50,ipady=50)
b1.config(command = lambda : ButtonClick(1))


b2 = ttk.Button(root, text=" ..",style ="my.TButton")
b2.grid(row=1, column=1, sticky="snew", ipadx=50, ipady=50)
b2.config(command = lambda : ButtonClick(2))

b3= ttk.Button(root, text=".. ",style="my.TButton")
b3.grid(row=1, column=2, sticky="snew", ipadx=50,
        ipady=50)
b3.config(command = lambda : ButtonClick(3))

b4 = ttk.Button(root, text=" ..",style="my.TButton")
b4.grid(row=2, column=0, sticky="snew", ipadx=50,
        ipady=50)
b4.config(command = lambda : ButtonClick(4))

b5 = ttk.Button(root, text=" ",style="my.TButton")
b5.grid(row=2, column=1, sticky="snew", ipadx=50,
        ipady=50)
b5.config(command = lambda : ButtonClick(5))

b6 = ttk.Button(root, text=".. ",style="my.TButton")
b6.grid(row=2, column=2, sticky="snew", ipadx=50,
        ipady=50)
b6.config(command = lambda : ButtonClick(6))

b7 = ttk.Button(root, text="..",style="my.TButton")
b7.grid(row=3, column=0, sticky="snew", ipadx=50,
        ipady=50)
b7.config(command = lambda : ButtonClick(7))

b8 = ttk.Button(root, text="..",style="my.TButton")
b8.grid(row=3, column=1, sticky="snew", ipadx=50,
        ipady=50)
b8.config(command = lambda : ButtonClick(8))

b9 = ttk.Button(root, text=" ..",style="my.TButton")
b9.grid(row=3, column=2, sticky="snew", ipadx=50,
        ipady=50)
b9.config(command = lambda : ButtonClick(9))

Button(text="New Game..", font=('georgia', 22, 'bold'), bg='blue', fg='black',
            border=5, width=4,command = lambda :Restart()).grid(row=0, column=1, sticky="we")
root.resizable(0,0)
root.mainloop()
