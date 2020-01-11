
    
from tkinter import *
root = Tk()

'''def clear():
    numb1.delete(0,END)
    numb2.delete(0,END)'''
    
Numb1 = Entry(root,borderwidth=1, relief="solid")
Numb2 = Entry(root,borderwidth=1, relief="solid")
Resbox = Entry(root,borderwidth=1, relief="solid")

def add():
    N1 = eval(Numb1.get())
    N2 = eval(Numb2.get())
    result = N1 + N2
    Resbox.insert(0, result)

def sub():
    N1 = eval(Numb1.get())
    N2 = eval(Numb2.get())
    result = N1 - N2
    Resbox.insert(0, result)
def times():
    N1 = eval(Numb1.get())
    N2 = eval(Numb2.get())
    result = N1 * N2
    Resbox.insert(0, result)
def div():
    N1 = eval(Numb1.get())
    N2 = eval(Numb2.get())
    result = N1 / N2
    Resbox.insert(0, result)    

label1 = Label(root,text="Input Number 1:")
label2 = Label(root,text="Input Number 2:" )
butadd = Button(root, text="+",command=add,padx=40)
butsub = Button(root, text="-",command=sub,padx=40)
buttimes = Button(root, text="*",command=times,padx=40)
butdiv = Button(root, text="/",command=div,padx=40)
res = Label(root,text="Result: ")
    #placement
label1.grid( row=0, column =0,padx=10,pady=10)
label2.grid( row=1, column =0,padx=10,pady=10)

Numb1.grid(row=0,column=1,padx=10,pady=10)
Numb2.grid( row=1, column =1,padx=10,pady=10)

butadd.grid( row=2, column =0,padx=10,pady=10)
butsub.grid( row=2, column =1,padx=10,pady=10)
buttimes.grid( row=2, column =2,padx=10,pady=10)
butdiv.grid( row=2, column =3,padx=10,pady=10)


res.grid( row=3, column=0)
Resbox.grid(row=3, column=1,pady=10)


root.mainloop
def clear():
    numb1.delete
    numb2.delete
