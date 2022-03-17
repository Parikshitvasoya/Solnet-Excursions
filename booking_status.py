##tkinter module is initialised
import tkinter as tk
##data module is imported
import data as dt
## global books are imported
global books

##tkinter module is initialised
root=tk.Tk()
f = tk.Frame(master=root, width=350, height=350,background="white")
##tkinter module is initialised
f.pack()
##tkinter module is initialised
b_1=tk.Button(text="Solent Excursions",background="lightgreen")
##tkinter module is initialised
b_1.pack()
##tkinter module is initialised


l1=tk.Label(root,text="Fill the requirements of bookings" )
##tkinter module is initialised
l1.pack()
##tkinter module is initialised


print(dt.books)
##tkinter module is initialised
l2=tk.Label(root,text="User_Id: initial_location: Destination_location: Vehicle: Status of booking: On hold: Checking availability")
##tkinter module is initialised
l2.pack()
##tkinter module is initialised


b1 = tk.Button(root, text="Close", command=root.destroy,background="yellow")
##tkinter module is initialised
b1.pack()
##tkinter module is initialised

root.mainloop()
##main function is initialised
