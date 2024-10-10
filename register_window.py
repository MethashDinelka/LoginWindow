import customtkinter as tk
import os
import sys

root2 = tk.CTk()

def submit():
    username = entry1.get()
    password = entry2.get()

    file1 = open("username.txt","w")
    file1.write(username)

    file2 = open("password.txt","w")
    file2.write(password)
    root2.destroy()

def resource_path(relative_path):
    """ Get the absolute path to the resource, whether in development or in PyInstaller bundle """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

width, height = 700, 300

display_width = root2.winfo_screenwidth()
display_height = root2.winfo_screenheight()
left = int((display_width / 2) - (width / 2))
top = int((display_height / 2) - (height / 2))

tk.set_appearance_mode("system")
root2.title("Register Window")
root2.iconbitmap(resource_path("icon.ico"))
root2.configure(fg_color="white")
root2.geometry(f"{width}x{height}+{left}+{top}")
root2.resizable(False, False)

label1 = tk.CTkLabel(root2, text="Enter An Username : ", text_color="blue", font=("Times New Roman", 30))
label1.pack()

entry1 = tk.CTkEntry(root2, placeholder_text="Enter An Username", width=300, height=30)
entry1.pack()

emptylab = tk.CTkLabel(root2, text=" ")
emptylab.pack()

emptylab2 = tk.CTkLabel(root2, text=" ")
emptylab2.pack()

label2 = tk.CTkLabel(root2, text="Enter A Password : ", text_color="blue", font=("Times New Roman", 30))
label2.pack()

entry2 = tk.CTkEntry(root2, placeholder_text="Enter A Password", width=300, height=30)
entry2.pack()

emptylab2 = tk.CTkLabel(root2, text=" ")
emptylab2.pack()

submit_button = tk.CTkButton(root2,text="Submit",text_color="black",fg_color="pink",font=("Times New Roman",25),command=submit)
submit_button.pack()

root2.mainloop()




