from tkinter import *

tk = Tk()
tk.geometry("300x250")
tk.title("МОТЕМАТІКА")

def plus_click():
    res = float(ent1.get()) + float(ent2.get())
    lbl_res.config(text="=" + str(res))


def minus_click():
    res = float(ent1.get()) - float(ent2.get())
    lbl_res.config(text="=" + str(res))


def multiply_click():
    res = float(ent1.get()) * float(ent2.get())
    lbl_res.config(text="=" + str(res))


def divide_click():
    res = float(ent1.get()) / float(ent2.get())
    lbl_res.config(text="=" + str(res))


lbl1 = Label(text="Перше число", font=("Arial", 10))
lbl1.place(x=20, y=20)

ent1 = Entry(bd=1)
ent1.place(x=120, y=20, width=120)

lbl2 = Label(text="Друге число", font=("Arial", 10))
lbl2.place(x=20, y=50)

ent2 = Entry(bd=1)
ent2.place(x=120, y=50, width=120)

btn1 = Button(text="Додавання", fg="red", bg="grey", command=plus_click)
btn1.place(x=20, y=90, width=100, height=25)

btn2 = Button(text="Віднімання", fg="red", bg="grey", command=minus_click)
btn2.place(x=20, y=125, width=100, height=25)

btn3 = Button(text="Множення", fg="red", bg="grey", command=multiply_click)
btn3.place(x=20, y=160, width=100, height=25)

btn4 = Button(text="Ділення", fg="red", bg="grey", command=divide_click)
btn4.place(x=20, y=195, width=100, height=25)

lbl_res = Label(text="", font=("Arial", 12))
lbl_res.place(x=150, y=125)

tk.mainloop()