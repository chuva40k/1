#ПОВНІСТЮ ГОТОВА ЄБОТНЯ
from tkinter import *
tk = Tk()
tk.geometry('400x300')
tk.title("Проект")
def button1_clicked():
    tk.geometry('800x400')
    tk['bg'] = 'green'
    button1['width'] = 30
    button1['bg'] = 'blue'
    button1['fg'] = 'white'
    button1['state'] = 'disabled'
    current_width = int(button2['width'])
    button2['width'] = current_width + 5
def button2_clicked():
    label['bg'] = 'red'
    label['width'] = 40
    label['fg'] = 'yellow'
    label['text'] = "Ми вивчаємо мову програмування Python!"
button1 = Button(tk, text="Вікно проекту", width=20, height=2, bg="grey", fg="yellow", command=button1_clicked)
button1.place(x=50, y=50)
button2 = Button(tk, text="Напис", width=10, height=3, bg="blue", fg="white", command=button2_clicked)
button2.place(x=250, y=50)
label = Label(tk, text="11-А2 клас", fg="blue", font=("Arial", 14))
label.place(x=50, y=150)
tk.mainloop()
