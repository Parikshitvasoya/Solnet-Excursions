##tkinter module is initialised for GUI
import tkinter as tk
import subprocess## subprocess package is initialised



def adv():##function is defined
    subprocess.call(["python","advisor.page.py"])
    ## function is called

def registration():
    subprocess.call(["python","registration.py"])
    ## registration page is called



def booking_status():##defining the booking function
    subprocess.call(["python","booking_status.py"])
    ## function is called


def summary():##defining the subprocess function
    subprocess.call(["python","summary.py"])
    ## function is called


root=tk.Tk()


f = tk.Frame(master=root, width=200, height=200,background="white")
##tkinter button is initiliased with height width and background color
f.pack()
##tkinter module is initiliased
b_1=tk.Button(text="Solent Excursions",background="yellow")
##tkinter button is initiliased with height width and background color
b_1.pack()##tkinter module is initiliased


b1=tk.Button(root,text="Confirm the location", command=adv,background="lightgreen")##Initializing the tkinter button with height width and background color
b1.pack()
##tkinter module is initiliased

b2=tk.Button(root,text="Show status of your booking", command=booking_status,background="lightgreen")
##tkinter button is initiliased with height width and background color
b2.pack()
##tkinter module is initiliased

b3=tk.Button(root,text="Booking Description", command=summary,background="lightgreen")
##tkinter button is initiliased with height width and background color
b3.pack()
##tkinter module is initiliased


b4=tk.Button(root,text="Booking Details", command=registration,background="lightgreen")
b4.pack()

b5=tk.Button(root,text="Exit", command=root.destroy,background="lightgreen")
##tkinter button is initiliased with height width and background color
b5.pack()
##tkinter module is initiliased


root.mainloop()
##mainfunction is initiliased