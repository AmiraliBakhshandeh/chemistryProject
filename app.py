from tkinter import *
import periodic_elems



def findit():
    val1 = entry1.get().capitalize()
    val2 = entry2.get().capitalize()
    
    

    execute = f"label1.config(text='{val1}:'+str(periodic_elems.Element().{val1}))"
    execute2 = f"label2.config(text='{val2}:'+str(periodic_elems.Element().{val2}))"

    exec(execute) 

    exec(execute2) 
    

tk = Tk()
tk.title("بدست آوردن پیوند یونی")

entry1  = Entry(width=200)
entry1.pack()
entry2  = Entry(width=200)
entry2.pack()

label1 = Label()
label1.pack()
label2 = Label()
label2.pack()
button = Button(text='get Elem',command=lambda:findit())
button.pack()
tk.mainloop()