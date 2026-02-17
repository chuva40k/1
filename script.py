from tkinter import *

tk = Tk()
tk.geometry("600x600")
tk.title("Вітальна листівка")

def btn1_click():
    global img
    if var.get() == 1:
        img = PhotoImage(file='flowers.png')
    if var.get() == 2:
        img = PhotoImage(file='cake.png')
    if var.get() == 3:
        img = PhotoImage(file='landscape.png')

    select = list(lbox.curselection())
    lbl2.config(text=ent.get() + ", " + lbox.get(select[0]))

    s = canvas.create_image(25, 180, anchor=NW, image=img)

lbl1 = Label(text="Ваше ім'я:")
lbl1.place(x=50, y=50)

ent = Entry(bd=1)
ent.place(x=120, y=50, width=120)

btn1 = Button(text="Привітання", command=btn1_click, bg="lightgrey")
btn1.place(x=50, y=100, width=100, height=40)

btn2 = Button(text="Вихід", command=tk.destroy, bg="lightgrey")
btn2.place(x=180, y=100, width=100, height=40)

lbl2 = Label(text="Тут буде привітання", font=("Arial", 12, "bold"))
lbl2.place(x=50, y=160)

lbl_list = Label(text="Вітання")
lbl_list.place(x=350, y=30)

lbox = Listbox(height=4)
lbox.insert(1, "З Днем народження!")
lbox.insert(2, "З Новим роком!")
lbox.insert(3, "З 8 березня!")
lbox.select_set(0)
lbox.place(x=350, y=50, width=150)

lbl_radio = Label(text="Зображення на листівку")
lbl_radio.place(x=350, y=150)

var = IntVar()
var.set(1)

r1 = Radiobutton(text="Квіти", variable=var, value=1)
r1.place(x=350, y=180)

r2 = Radiobutton(text="Торт", variable=var, value=2)
r2.place(x=350, y=210)

r3 = Radiobutton(text="Пейзаж", variable=var, value=3)
r3.place(x=350, y=240)

canvas = Canvas(tk, width=400, height=400, bg="white")
canvas.place(x=50, y=200)

tk.mainloop()