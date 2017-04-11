from tkinter import *

root = Tk()

def right_click(event):
    print("Right")


def middle_click(event):
    print("Middle")


def left_click(event):
    print("Left")

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", left_click)
frame.bind("<Button-2>", middle_click)
frame.bind("<Button-3>", right_click)
frame.pack()




"""
def print_name(event):
    print("Hello, my name is Darvis!")


button1 = Button(root, text="Print my name")
button1.bind("<Button-1>", print_name)
button1.pack()
"""


root.mainloop()