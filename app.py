from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox
import periodic_elems
import alghorithm
import turtle
import json





def findit():
    messagebox.showinfo("راهنما", "با سلام استاد شاهی عزیز . این نرم افزار توسط امیرعلی بخشنده و پندار احمدی 903 ساخته شده است. این نرم افزار توانایی نشان دادن تمامی عناصر جدول تناوبی را در مدل بور  دارد که روز ها برای آن زحمت کشیده شده است . امیدواریم از آن لذت ببرید")

    val1 = e1.get().capitalize()
    val2 = e2.get().capitalize()
    draw = turtle.RawTurtle(canvas)
    draw2 = turtle.RawTurtle(canvas2)
    list1 = "alghorithm.Bohr(periodic_elems.Element()."+val1+")"
    list2 = "alghorithm.Bohr(periodic_elems.Element()."+val2+")"
    bohr1 = eval(list1)
    bohr2 = eval(list2)
    ionCompound = alghorithm.IonCompound(val1, val2, bohr1[-1], bohr2[-1])



    
    s1 = ""
    s2 = ""
    list3 = []
    list4 = []

    
    
    for x in bohr1 :
        if x != 0:
            s1+=str(x)+") "
            list3.append(x)
    for x in bohr2 :
        if x != 0:
            s2+=str(x)+") "
            list4.append(x)



    l3.config(text=f"{val1} : "+ s1)
    l4.config(text=f"{val2} : "+ s2)
    l6.config(text=' تناوب :'+str(len(list3))+ ' گروه : ' + str(list3[-1]))
    l7.config(text=' تناوب :'+str(len(list4))+ ' گروه : ' + str(list4[-1]))
    l8.config(text=val1)
    l9.config(text=val2)
    
    alghorithm.Circle(draw, list3)
    alghorithm.Circle(draw2, list4)


master = Tk()

e1 = Entry(master)
e2 = Entry(master)
button = Button(text='بدست آوردن اطلاعات عنصرها',command=lambda:findit())
l1 = Label(master, text = "اولین عنصر:")
l2 = Label(master, text = "دومین عنصر:")
l5 = Label(master, text="اطلاعات عناصر:")
l3 = Label()
l4 = Label()
l6 = Label()
l7 = Label()
l8 = Label()
l9 = Label()
canvas = Canvas(master, width = 200, height = 200)
canvas2 = Canvas(master, width = 200, height = 200)

l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)
e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)
button.grid(row = 2, column = 0, pady = 1)
l3.grid(row = 4, column = 0, pady = 2)
l4.grid(row = 5, column = 0, pady = 2)
l5.grid(row = 3,column=0,pady = 2)
l6.grid(row = 4,column=1,pady = 2)
l7.grid(row = 5,column=1,pady = 2)
l8.grid(row = 7,column=0,pady = 2)
l9.grid(row = 7,column=1,pady = 2)
canvas.grid(row=8, column=0,pady=2) 
canvas2.grid (row=8, column=1) 


master.mainloop()
