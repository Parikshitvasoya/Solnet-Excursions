import tkinter as tk ## PACKAGE FOR GUI
import subprocess## SUBPROCESS IS IMPORTED.

def fun1():##FUNCTION IS DEFINED
    subprocess.call(["python","C:\\Users\\admin\\PycharmProjects\\Solent_Camp\\cust_login.py"])##Call the function

def fun2():##FUNCTION IS DEFINED
    subprocess.call(["python","C:\\Users\\admin\\PycharmProjects\\Solent_Camp\\Admin_login.py"])##Call the function

root=tk.Tk()## tkinter module is initialized

f = tk.Frame(master=root,width=350, height=350,background="white")##tkinter module is initialized with height background
f.pack() ##tkinter module is initialized
b_1=tk.Button(text="SOLENT EXCURSIONS",background="yellow")##tkinter module is initialized with height and background
b_1.pack()##button function is used


b1=tk.Button(text="CUSTOMERS", command=fun1,background="PINK")##tkinter module is initialized with height and background
b1.pack()##button function is used


b2=tk.Button(text="ADMIN", command=fun2,background="PINK")##Initializing the tkinter button with height width and background color
b2.pack()##calling the button function


root.mainloop()##calling the mainloop function


