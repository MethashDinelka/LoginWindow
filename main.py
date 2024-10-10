import customtkinter as tk
import subprocess
import threading
import os
import sys

root= tk.CTk()

def resource_path(relative_path):
    """ Get the absolute path to the resource, whether in development or in PyInstaller bundle """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def register_fix():
    threading.Thread(target=register).start()

def register():
    subprocess.run(["python","register_window.py"])

def last_fix():
    threading.Thread(target=last).start()

def last():
    subprocess.run(["python", "welcome.py"])


def login():
    uname = entry_username.get()
    psw = entry_password.get()

    file1 = open("username.txt","r")
    username = file1.read()

    file2 = open("password.txt","r")
    password = file2.read()

    if (uname==username)and(psw==password):
        last_fix()
        root.destroy()
    else:
        emptylab2.configure(text="Incorrect Username or Password! Check Again",text_color="red")

width, height = 700, 630

display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()
left = int((display_width / 2) - (width / 2))
top = int((display_height / 2) - (height / 2))

tk.set_appearance_mode("system")
root.title("Welcome ! ")
root.iconbitmap(resource_path("icon.ico"))
root.configure(fg_color="white")
root.geometry(f"{width}x{height}+{left}+{top}")
root.resizable(False, False)

label_main = tk.CTkLabel(root,text="Welcome To The Login Page !",font=("Times New Roman",50),text_color="red",fg_color="transparent")
label_main.pack()

label_username = tk.CTkLabel(root,text="Username : ",font=("Times New Roman",40),text_color="green",fg_color="transparent")
label_username.pack(pady=10)

entry_username = tk.CTkEntry(root,width=300,placeholder_text="Enter Your Username",height=40,placeholder_text_color="white")
entry_username.pack(padx=20)

label_password = tk.CTkLabel(root,text="Password : ",font=("Times New Roman",40),text_color="green",fg_color="transparent")
label_password.pack(pady=20)

entry_password = tk.CTkEntry(root,width=300,placeholder_text="Enter Your Password",height=40,placeholder_text_color="white")
entry_password.pack(padx=20)

emptylab2 = tk.CTkLabel(root,)
emptylab2.configure(text=" ")
emptylab2.pack()

login_button = tk.CTkButton(root,text="Login",width=250,height=60,fg_color="orange",text_color="white",font=("Aerial",40),command=login)
login_button.pack(pady=40)

reg_button = tk.CTkButton(root,text="Register",width=250,height=60,fg_color="orange",text_color="white",font=("Aerial",40),command=register_fix)
reg_button.pack(pady=20)

close_button = tk.CTkButton(root,text="Close",width=250,height=60,fg_color="red",text_color="white",font=("Aerial",40),command=lambda :root.destroy()).pack()
root.mainloop()
