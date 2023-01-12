from tkinter import * 
from tkinter.ttk import *
import periodic_elems
import alghorithm



def findit():
    val1 = e1.get().capitalize()
    val2 = e2.get().capitalize()
    
    

    execute = f"l3.config(text='{val1} : ' + str(alghorithm.Bohr(periodic_elems.Element().{val1})))"
    execute2 = f"l4.config(text='{val2} : ' + str(alghorithm.Bohr(periodic_elems.Element().{val2})))"
    s1 = ""
    list1 = "s1 = str(alghorithm.Bohr(periodic_elems.Element()."+val1+"))"
    exec(list1)
    print(s1)
    exec(execute) 
    exec(execute2) 


    

master = Tk()

e1 = Entry(master)
e2 = Entry(master)
button = Button(text='بدست آوردن اطلاعات عنصرها',command=lambda:findit())
l1 = Label(master, text = "اولین عنصر:")
l2 = Label(master, text = "دومین عنصر:")
l3 = Label()
l4 = Label()
l5 = Label(master)



l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)
e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)
button.grid(row = 2, column = 0, pady = 2)
l3.grid(row = 3, column = 0, pady = 2)
l4.grid(row = 4, column = 0, pady = 2)
l5.grid(row = 5,column=0,pady = 2)

mainloop()
