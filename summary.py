import tkinter as tk


root=tk.Tk()
f = tk.Frame(master=root, width=300, height=300,background="white")
f.pack()
b_1=tk.Button(text="Solent Excursions",background="yellow")
b_1.pack()

l1=tk.Label(root,text="Description of your booking")
l1.pack()

l2=tk.Label(root,text="Trip_id: , User_Id:, Start_location:, Drop_location:, Trip_package_id:, Rate:, Status of booking: Confirmed by administration" )
l2.pack()

root.mainloop()
