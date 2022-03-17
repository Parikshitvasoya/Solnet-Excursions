import tkinter as tk##Initializing the tkinter module
import subprocess## Importing the subprocess package
import data as dt## Importing the data file from the date file

def fun():##Initializing the tkinter module
    print(clicked.get())##ing the tkinter module
    if clicked.get() == 'personalised car':##Initializing the tkinter module
        options1 = ["1-person", "2-persons", "2-persons", "more than 3"]##tkinter module is initialised
        clicked1 = tk.StringVar()##tkinter module is initialised
        drop1 = tk.OptionMenu(root, clicked1, *options1)##tkinter module is initialised
        drop1.pack()##tkinter module is initialised

def save():##tkinter module is initialised
    root.destroy##tkinter module is initialised


root=tk.Tk()##tkinter module is initialised

f = tk.Frame(master=root, width=300, height=300,background="")##tkinter module is initialised
f.pack()##Initialize the tkinter module
b_1=tk.Button(text="Solent Excursions",background="pink")##Initialize the tkinter module
b_1.pack()##tkinter module is initialised


l1=tk.Label(root,text="Enter Initial_location: ",background="yellow")##tkinter module is initialised
l1.pack()##tkinter module is initialised
tb1 = tk.Text(root, height = 1, width = 15)##tkinter module is initialised
tb1.pack()##Initialize the tkinter module

l2=tk.Label(root,text="Enter Destination_location: ",background="yellow")##tkinter module is initialised
l2.pack()##Initializing the tkinter module
tb2 = tk.Text(root, height = 1, width = 15)##tkinter module is initialised
tb2.pack()##tkinter module is initialised

l3=tk.Label(root,text="choose the vehicle : ",background="yellow")##tkinter module is initialised
l3.pack()##tkinter module is initialised
clicked = tk.StringVar()##tkinter module is initialised
options=["scorpio","innova","jeep"]##tkinter module is initialised
drop = tk.OptionMenu( root , clicked , *options)##tkinter module is initialised
drop.pack()##tkinter module is initialised

b1=tk.Button(text="Enter", command=fun,background="lightgreen")##tkinter module is initialised
b1.pack()##tkinter module is initialised


root.mainloop()##tkinter module is initialised
