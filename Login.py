import tkinter as tk
from tkinter import messagebox

import databaseManager
import main
import userlogin.en_decrypter


# Function to handle login button click
def login():
    name = name_entry.get()
    password = password_entry.get()

    if userlogin.en_decrypter.encode(password) == databaseManager.getUserByName(name)[0][3]:  # Simple condition for demonstration
        root.destroy()
        main.mainWindow()
    else:
        messagebox.showwarning("Login", "Invalid Credentials")

# Create the main application window
root = tk.Tk()
root.title("Login Form")

# Set the window size
root.geometry("300x200")

# Add a label for Name
name_label = tk.Label(root, text="Name")
name_label.pack(pady=10)

# Add an entry box for Name
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Add a label for Password
password_label = tk.Label(root, text="Password")
password_label.pack(pady=10)

# Add an entry box for Password, with the show='*' to hide the password characters
password_entry = tk.Entry(root, show='*')
password_entry.pack(pady=5)

# Add a login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)

root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())

# Start the application
root.mainloop()
