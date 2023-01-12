from tkinter import *
from tkinter import ttk
import json

tk = Tk()
command = {
	
}

tk.title("Chemistry Project")



label = Label(tk,text="لطفا یکی از شرایط زیر را انتخاب بکنید")
label.pack()

combo = ttk.Combobox(width=100,values=["دما صعودی"," دما نزولی","رسوب"])
combo.pack()



tk.mainloop()