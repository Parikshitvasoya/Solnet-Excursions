import tkinter as tk ##Initialize the tkinter module
import subprocess ##Initialize the subprocess module
import data as dt
##windows form is initialized
window = tk.Tk()

window.title("Details of booking")

## defining the inserting item
def insertitem():
    listbox.insert(tk.END,content.get())

##defining the delete item
def deleteitem():
    listbox.delete(0, tk.END)
##defining the delete item that are selected
def deleteitemselected():
    listbox.delete(tk.ANCHOR)
window.geometry("400x400")
window.configure(bg='#117fed')
##adding button
label = tk.Label(window, text = "Insert the details",background='#6dd1b6', width=100, height=2)
label.pack()
button = tk.Button(window,text = "Insert Details", command=insertitem, background="#34a312", foreground='white')
button.pack()
##adding the delete button
button_delete = tk.Button(window,text = "Delete Details", command=deleteitem,background="#34a312", foreground='white')
button_delete.pack()

##adding the selected delete button
button_delete_selected = tk.Button(window, text="Delete selected Details",background="#34a312", foreground='white', command=deleteitemselected)
button_delete_selected.pack()

content = tk.StringVar()
entry = tk.Entry(window, textvariable=content)
entry.pack()

listbox = tk.Listbox(window)
listbox.pack()
window.mainloop()

## creating class
class solent:
    id = 0
    name = ""
    def display(self,id,name):
        self.id = id
        self.name = name
        print(self.id, self.name)
csa=solent()
csa.display(1,"Welcome to the camp booking sites- Solent Excursions")


def fun():##tkinter module is initiliased
    subprocess.call(["python","customer.py"])##tkinter module is initiliased

##tkinter module is initiliased
root=tk.Tk()
root.geometry("400x400")
root.configure(bg='#117fed')

# f = tk.Frame(root,width=200, height=200,background="#02c6f7")
# f.pack()

b_1=tk.Label(text="Solent Excursions",background="#6dd1b6", height=2, width=100)
b_1.pack()

l=tk.Label(root,text="Administrator Sign in and", background='#a2b8b2',borderwidth=1)
l.pack()
l1=tk.Label(root,text="Sign up: ", background='#a2b8b2')
l1.pack()
tb1 = tk.Text(root, height = 1, width = 20, borderwidth=1,)
tb1.pack()


l2 = tk.Label(root,text="Enter password: ",background='#a2b8b2')
##tkinter module is initiliased
l2.pack()
##tkinter module is initiliased

e1 = tk.Entry(root, show="*", width=20)
##tkinter module is initiliased
e1.pack()
##tkinter module is initiliased


b1 = tk.Button(text="Submit", command=fun, background="#34a312", foreground='white')
##tkinter module is initiliased
b1.pack()

root.mainloop()
##mainfunction is initiliased




