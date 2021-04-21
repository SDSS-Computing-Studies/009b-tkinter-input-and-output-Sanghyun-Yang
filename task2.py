"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""

import tkinter as tk
from tkinter import *

win = tk.Tk()

eoutput = StringVar()
eoutput.set("Answer")

sign1 = StringVar()
sign1.set("-")
sign2 = StringVar()
sign2.set("+")

def trinomial():
    a = 1
    b = int(e1.get())
    c = int(e2.get())

    a1 = (-b + (b**2-4*a*c) ** (1/2)) / (2)
    a2 = (-b - (b**2-4*a*c) ** (1/2)) / (2)

    o1 = -1*a1
    o2 = -1*a2

    x = str(o1)
    y = str(o2)

    if o1 > 0 and o2 > 0:
        o3 = "(x + " + x + ")" + "(x + " + y + ")"
    elif o1 > 0 and o2 < 0:
        o3 = "(x + " + x + ")" + "(x" + y + ")"
    elif o1 < 0 and o2 < 0:
        o3 = "(x" + x + ")" + "(x" + y + ")"
    elif o1< 0 and o2 > 0:
        o3 = "(x" + x + ")" + "(x + " + y + ")"    



    p1.delete(0, END)
    p1.insert(0, o3)

def i1():
    cs = sign1.get()
    if cs == "-":
        sign1.set("+")
    elif cs == "+":
        sign1.set("-")

def i2():
    cs2 = sign2.get()
    if cs2 == "-":
        sign2.set("+")
    elif cs2 == "+":    
        sign2.set("-")

l1 = Label(win, text="Input Value For B And C (A Will Always Be 1)")
l2 = Label(win, text="ax^2")
l3 = Label(win, text="x")
b1 = Button(win, text="=", command=trinomial)
b2 = Button(win, textvariable=sign1, command=i1)
b3 = Button(win, textvariable=sign2, command=i2)
e1 = Entry(win, text="B")
e2 = Entry(win, text="C")
p1 = Entry(win, text="Answer", textvariable=eoutput)

l1.pack()
l2.pack(side=LEFT)
b2.pack(side=LEFT)
e1.pack(side=LEFT)
l3.pack(side=LEFT)
b3.pack(side=LEFT)
e2.pack(side=LEFT)
b1.pack(side=LEFT)
p1.pack()

win.mainloop()