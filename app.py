from tkinter import *
from tkinter import ttk
import json


def first()
    return 0
def second():
    return 0
def third():
    return 0

tk = Tk()
command = {
    "رسوب":first,
    "دما نزولی":second,
    "دما صعودی":third 
}

tk.title("Chemistry Project")



label = Label(tk,text="لطفا یکی از شرایط زیر را انتخاب بکنید")
label.pack()

combo = ttk.Combobox(width=100,values=["دما صعودی","دما نزولی","رسوب"])
combo.pack()

command[combo]()

tk.mainloop()