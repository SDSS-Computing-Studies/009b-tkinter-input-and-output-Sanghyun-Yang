"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""

import tkinter as tk
from tkinter import *

win = tk.Tk()

f1 = Frame()
l1 = Label(f1, text="Enter a Adjective: ")
e1 = Entry(f1, text="Adjective")

f2 = Frame()
l2 = Label(f2, text="Enter a Name: ")
e2 = Entry(f2, text="Name")

f3 = Frame()
l3 = Label(f3, text="Enter a Noun: ")
e3 = Entry(f3, text="Noun")

f4 = Frame()
l4 = Label(f4, text="Enter a Plural Noun: ")
e4 = Entry(f4, text="Plural Noun")

f5 = Frame()
l5 = Label(f5, text="Enter a Adjective: ")
e5 = Entry(f5, text="Adjective2")

b1 = Button

o1 = StringVar()
o2 = StringVar()
o3 = StringVar()
o4 = StringVar()
o5 = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()


def madLibs():
    a1 = e1.get()
    o1.set(a1)

    a2 = e2.get()
    o2.set(a2)

    a3 = e3.get()
    o3.set(a3)

    a4 = e4.get()
    o4.set(a4)

    a5 = e5.get()
    o5.set(a5)

    t1.set("Theres this")
    t2.set("guy named")
    t3.set("who brings")
    t4.set("to all the")
    t5.set("who've been")


b1 = Button(win, text="Click To Create Madlib", command=madLibs)

ff1 = Frame()
ffl1 = Label(ff1, textvariable=t1)
ffl2 = Label(ff1, textvariable=o1)

ff2 = Frame()
ffl3 = Label(ff2, textvariable=t2)
ffl4 = Label(ff2, textvariable=o2)

ff3 = Frame()
ffl5 = Label(ff3, textvariable=t3)
ffl6 = Label(ff3, textvariable=o3)

ff4 = Frame()
ffl7 = Label(ff4, textvariable=t4)
ffl8 = Label(ff4, textvariable=o4)

ff5 = Frame()
ffl9 = Label(ff5, textvariable=t5)
ffl10 = Label(ff5, textvariable=o5)


f1.pack()
l1.pack(side=LEFT)
e1.pack(side=LEFT)

f2.pack()
l2.pack(side=LEFT)
e2.pack(side=LEFT)

f3.pack()
l3.pack(side=LEFT)
e3.pack(side=LEFT)

f4.pack()
l4.pack(side=LEFT)
e4.pack(side=LEFT)

f5.pack()
l5.pack(side=LEFT)
e5.pack(side=LEFT)

b1.pack()

ff1.pack()
ffl1.pack(side=LEFT)
ffl2.pack(side=LEFT)

ff2.pack()
ffl3.pack(side=LEFT)
ffl4.pack(side=LEFT)

ff3.pack()
ffl5.pack(side=LEFT)
ffl6.pack(side=LEFT)

ff4.pack()
ffl7.pack(side=LEFT)
ffl8.pack(side=LEFT)

ff5.pack()
ffl9.pack(side=LEFT)
ffl10.pack(side=LEFT)


win.mainloop()