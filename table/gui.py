import tkinter as tk

import databaseManager
from table import addRowWindow, deleteRow, editRowWindow
from tkinter import ttk

# Global variables for buttons and treeview_table
button1 = None
button2 = None
button3 = None
treeview = None


# Function to sort the Treeview column and update the header indicator
def sort_column(treeview_table, col, reverse):
    # Remove current indicators
    for heading in treeview_table["columns"]:
        current_text = treeview_table.heading(heading, "text")
        # Remove any existing indicators
        if current_text.endswith("▲") or current_text.endswith("▼"):
            treeview_table.heading(heading, text=current_text[:-1])

    # Get the data from the Treeview
    data = [(treeview_table.set(item, col), item) for item in treeview_table.get_children('')]

    # Sort data
    data.sort(reverse=reverse)

    # Rearrange items in sorted positions
    for index, (val, item) in enumerate(data):
        treeview_table.move(item, '', index)

    # Update the column heading with the sorting indicator
    if reverse:
        treeview_table.heading(col, text=treeview_table.heading(col, "text") + "▲")
    else:
        treeview_table.heading(col, text=treeview_table.heading(col, "text") + "▼")

    # Reverse the sort order for the next click
    treeview_table.heading(col, command=lambda: sort_column(treeview_table, col, not reverse))


# Define light and dark themes
def set_light_theme(root: tk.Tk):
    style = ttk.Style()
    style.theme_use("clam")
    root.configure(bg='white')
    button1.configure(bg='lightgrey', fg='black')
    button2.configure(bg='lightgrey', fg='black')
    button3.configure(bg='lightgrey', fg='black')
    style.configure("Treeview", background="lightgrey", fieldbackground="lightgrey", foreground="black")


def set_dark_theme(root: tk.Tk):
    style = ttk.Style()
    style.theme_use("clam")
    root.configure(bg='#2e2e2e')
    button1.configure(bg='#3c3c3c', fg='white')
    button2.configure(bg='#3c3c3c', fg='white')
    button3.configure(bg='#3c3c3c', fg='white')
    style.configure("Treeview", background="#3c3c3c", fieldbackground="#3c3c3c", foreground="white")


def create_table(root):
    global button1, button2, button3, table

    # Create a Treeview widget for the table
    table = ttk.Treeview(root, columns=("ID", "ServiceTag", "Type", "Raum"), show='headings')

    # Define the column headings with initial text
    table.heading("ID", text="ID", command=lambda: sort_column(table, "ID", False))
    table.heading("ServiceTag", text="ServiceTag", command=lambda: sort_column(table, "ServiceTag", False))
    table.heading("Type", text="Type", command=lambda: sort_column(table, "Type", False))
    table.heading("Raum", text="Raum", command=lambda: sort_column(table, "Raum", False))

    # Define the column widths
    table.column("ID", width=150, anchor='center')
    table.column("ServiceTag", width=100, anchor='center')
    table.column("Type", width=150, anchor='center')
    table.column("Raum", width=150, anchor='center')

    # Add data to the table
    data = databaseManager.getAllRowsAsList()

    for row in data:
        table.insert("", tk.END, values=row)

    # Place the table in the grid
    table.grid(row=0, column=1, padx=20, pady=40, rowspan=5, sticky="nsew")

    # Create buttons
    button1 = tk.Button(root, text="Add", command=lambda: addRowWindow.openWindow(table))
    button2 = tk.Button(root, text="Edit", command=lambda: editRowWindow.openWindow(table))
    button3 = tk.Button(root, text="Delete", command=lambda: deleteRow.deleteSelectedRow(table))

    # Place buttons in the third column (25% space), centered vertically with equal space
    button1.grid(row=1, column=2, padx=20, pady=2, sticky="ew")
    button2.grid(row=2, column=2, padx=20, pady=2, sticky="ew")
    button3.grid(row=3, column=2, padx=20, pady=2, sticky="ew")


def update_table(new_data):
    # Clear existing data in the table
    for row in table.get_children():
        table.delete(row)

    # Insert new data into the table
    for row in new_data:
        table.insert("", tk.END, values=row)
