import customtkinter as tk
import webbrowser
import os
import sys

root = tk.CTk()
def resource_path(relative_path):
    """ Get the absolute path to the resource, whether in development or in PyInstaller bundle """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

width, height = 700 , 300

display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()
left = int((display_width / 2) - (width / 2))
top = int((display_height / 2) - (height / 2))

tk.set_appearance_mode("system")
root.title("Register Window")
root.iconbitmap(resource_path("icon.ico"))
root.geometry(f"{width}x{height}+{left}+{top}")
root.resizable(False, False)

label = tk.CTkLabel(root,text="You're Successfully Logged In ! ^o^",font=("Times New Roman",40),text_color="yellow")
label.pack()

label2 = tk.CTkLabel(root,text="Methash Dinelka - Software Development").pack()
label3 = tk.CTkLabel(root,text="https://methash-dinelka.blogspot.com/").pack()

emptylab2 = tk.CTkLabel(root, text=" ")
emptylab2.pack()

button = tk.CTkButton(root,text="Close",fg_color="red",text_color="white",font=("Aerial",20),width=75,height=15,command=lambda :root.destroy()).pack(pady=10)

button2 = tk.CTkButton(root,text="Website",fg_color="blue",text_color="white",font=("Aerial",20),width=75,height=15,command=lambda :webbrowser.open("https://methash-dinelka.blogspot.com/")).pack(pady=10)

button3 = tk.CTkButton(root,text="Github",fg_color="blue",text_color="white",font=("Aerial",20),width=75,height=15,command=lambda :webbrowser.open("https://github.com/MethashDinelka")).pack(pady=10)
root.mainloop()