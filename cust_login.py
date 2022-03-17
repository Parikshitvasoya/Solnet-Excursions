##tkinter is imported
import tkinter as tk

import subprocess
## subprocess package is imported
import data as dt
## data is imported


def fun():
    ##function is defined
    dt.cust_id=tb1.get("1.0", "end-1c")
    ##function is called
    root.destroy
    ##function is called
    subprocess.call(["python","customer.py"])
    ##subprocess is called


root=tk.Tk()
##function is called

f = tk.Frame(master=root, width=300, height=300,background="white")
##tkinter button is initiliased with height width and background color
f.pack()
##tkinter button is initiliased
b_1=tk.Button(text="Solent Excursions",background="pink")
##tkinter button is initiliased with height width and background color
b_1.pack()
##tkinter button is initiliased


l=tk.Label(root,text="Sign in page for Users" )
##tkinter button is initiliased with height width and background color
l.pack()
##tkinter button is initiliased

l1=tk.Label(root,text="Sign in: " ,background="yellow")
##tkinter button is initiliased with height width and background color
l1.pack()
##tkinter button is initiliased
tb1 = tk.Text(root, height = 2, width = 20)
##tkinter button is initiliased with height width and background color
tb1.pack()
##tkinter button is initiliased



l2=tk.Label(root,text="Enter the password: ",background="yellow" )
##tkinter button is initiliased with height width and background color
l2.pack()
##tkinter button is initiliased

e1=tk.Entry(root, show="*", width=30)
##tkinter button is initiliased with height width and background color
e1.pack()
##tkinter button is initiliased


b1=tk.Button(text="Click", command=fun)
##tkinter button is initiliased with height width and background color
b1.pack()
##tkinter button is initiliased
root.mainloop()
##mainfunction is initiliased

