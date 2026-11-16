import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Login Form")
root.geometry("1000x750")

bg = tk.PhotoImage(file="background_img.png")

canvas = tk.Canvas(
    root,
    width=1000,
    height=750,
    highlightthickness=0
)
canvas.pack(fill="both", expand=True)

canvas.create_image(0, 0, image=bg, anchor="nw")

canvas.create_text(
    530, 150,
    text="LOGIN",
    font=("Arial", 35, "bold"),
    fill="white"
)

canvas.create_text(
    530, 230,
    text="Welcome Back! Please login",
    font=("Arial", 14),
    fill="white"
)

canvas.create_text(
    375, 290,
    text="Username",
    font=("Arial", 12),
    fill="#699EDF",
    anchor="w"
)

username_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=35,
    bd=0
)
username_entry.place(x=375, y=315, width=325, height=38)

canvas.create_text(
    375, 390,
    text="Password",
    font=("Arial", 12),
    fill="#699EDF",
    anchor="w"
)

password_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=35,
    bd=0,
    show="*"
)
password_entry.place(x=375, y=415, width=325, height=38)

def messagebox(message):

    window = tk.Toplevel(root)
    window.title("Login")
    window.geometry("300x150")

    window.update_idletasks()

    x = root.winfo_x() + (root.winfo_width() - 300) // 2
    y = root.winfo_y() + (root.winfo_height() - 150) // 2

    window.geometry(f"300x150+{x}+{y}")
    window.configure(bg="#071B38")

    tk.Label(
        window,
        text=message,
        font=("Arial", 12),
        fg="white",
        bg="#071B38"
    ).pack(pady=30)

    tk.Button(
        window,
        text="OK",
        command=window.destroy
    ).pack()

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "12345":
        messagebox("Welcome Admin!")
    else:
        messagebox("Invalid Username and Password!")

login_button = tk.Button(
    root,
    text="LOG IN",
    font=("Arial", 13, "bold"),
    bg="#1769D2",
    fg="white",
    activebackground="#0D55B0",
    activeforeground="white",
    bd=0,
    cursor="hand2",
    command=login
)

login_button.place(
    x=375,
    y=495,
    width=325,
    height=55
)

root.mainloop()