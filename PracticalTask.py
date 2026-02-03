import tkinter as tk
root = tk.Tk()
root.title("Проект Python")
root.geometry("400x300")
def button1_click():
    root.geometry("800x400")
    root.configure(bg="green")
    btn1.config(width=30, bg="blue", fg="white", state="disabled")
    current_width = btn2.cget("width")
    btn2.config(width=current_width + 5)



def button2_click():

    label.config(
        bg="red",
        width=40,
        fg="yellow",
        text="Ми вивчаємо мову програмування Python!"
    )



btn1 = tk.Button(
    root,
    text="Вікно проекту",
    bg="grey",
    fg="yellow",
    width=20,
    height=2,
    command=button1_click
)
btn1.pack(pady=10)


btn2 = tk.Button(
    root,
    text="Напис",
    bg="blue",
    fg="white",
    width=10,
    height=3,
    command=button2_click  # прив'язка обробника події
)
btn2.pack(pady=10)

label = tk.Label(
    root,
    text="11-А1 клас",
    fg="blue",
    font=("Arial", 14)
)
label.pack(pady=10)

root.mainloop()