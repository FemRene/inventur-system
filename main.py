import tkinter as tk
from tkinter import ttk

from awthemes import AwthemesStyle

import table.gui
from table.gui import create_table
from treeview.gui import create_tree


# Define light and dark themes
def set_light_theme():
    style = AwthemesStyle(root)
    style.theme_use("awlight")
    root.configure(bg='white')
    theme_button.configure(bg='lightgrey', fg='black')
    types_button.configure(bg='lightgrey', fg='black')
    table.gui.set_light_theme(root)
    header_label.configure(bg='lightgrey', fg='black')

def set_dark_theme():
    style = AwthemesStyle(root)
    style.theme_use("awdark")
    root.configure(bg='#2e2e2e')
    theme_button.configure(bg='#3c3c3c', fg='white')
    types_button.configure(bg='#3c3c3c', fg='white')
    table.gui.set_dark_theme(root)
    header_label.configure(bg='#3c3c3c', fg='white')

def toggle_theme():
    global dark_mode
    if not dark_mode:
        set_light_theme()
    else:
        set_dark_theme()
    dark_mode = not dark_mode

import Login

def mainWindow():
    global dark_mode, root, types_button, theme_button, header_label
    # Create the root window
    root = tk.Tk()
    root.title("Inventar System")

    # Set the minimum window size (optional)
    root.minsize(600, 300)  # Minimum size to prevent collapsing

    # Create a Style object to configure theme styles
    root.style = ttk.Style()

    # Define
    dark_mode = False
    create_table(root)
    create_tree(root)
    # Configure grid layout: 25% for the empty field, 50% for the table, 25% for buttons
    root.grid_columnconfigure(0, weight=1)  # 25% for empty field
    root.grid_columnconfigure(1, weight=3)  # 50% for the table
    root.grid_columnconfigure(2, weight=1)  # 25% for buttons

    # Configure row expansion (add spacers to center the buttons)
    root.grid_rowconfigure(0, weight=1)  # Spacer row at the top to push buttons down
    root.grid_rowconfigure(1, weight=0)  # Button row
    root.grid_rowconfigure(2, weight=0)  # Button row
    root.grid_rowconfigure(3, weight=0)  # Button row
    root.grid_rowconfigure(4, weight=1)  # Spacer row at the bottom to push buttons up

    # Add a header label
    header_label = tk.Label(root, text="Inventar System", font=("Arial", 24), bg="gray", fg="white")
    header_label.grid(row=0, column=0, columnspan=3, padx=20, pady=0, sticky="new")

    # Add the theme toggle button
    theme_button = tk.Button(root, text="Toggle Theme", command=lambda: toggle_theme())
    theme_button.grid(row=0, column=2, padx=20, pady=(50, 20), sticky="ne")

    types_button = tk.Button(root, text="Edit Types")
    types_button.grid(row=0, column=2, padx=20, pady=80, sticky="ne")

    # Apply initial theme
    set_dark_theme()

    # Run the application
    root.mainloop()
