from tkinter import *

root = Tk()

label_name = Label(root, text="Name")
label_pass = Label(root, text="Password")

entry_name = Entry(root)
entry_pass = Entry(root)

label_name.grid(row=0, sticky=E) #sticky=E makes label text right-aligned
label_pass.grid(row=1, sticky=E)
entry_name.grid(row=0, column=1)
entry_pass.grid(row=1, column=1)

cbox_logged_in = Checkbutton(root, text="Keep me logged in")
cbox_logged_in.grid(columnspan=2)  #columnspan=2 means it will cover two columns




"""
one = Label(text="One", bg="red", fg="white")
one.pack()
two = Label(text="Two", bg="green", fg="black")
two.pack(fill=X)
three = Label(text="Three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)
"""



root.mainloop()