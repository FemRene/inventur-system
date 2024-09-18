import tkinter as tk

import databaseManager
import table.gui
from tkinter import ttk
from awthemes import AwthemesStyle

treeview: ttk.Treeview

def sort_column(treeview, col, reverse):
    # Remove current indicators
    for heading in treeview["columns"]:
        current_text = treeview.heading(heading, "text")
        # Remove any existing indicators
        if current_text.endswith("▲") or current_text.endswith("▼"):
            treeview.heading(heading, text=current_text[:-1])

    # Get the data from the Treeview
    data = [(treeview.set(item, col), item) for item in treeview.get_children('')]

    # Sort data
    data.sort(reverse=reverse)

    # Rearrange items in sorted positions
    for index, (val, item) in enumerate(data):
        treeview.move(item, '', index)

    # Update the column heading with the sorting indicator
    if reverse:
        treeview.heading(col, text=treeview.heading(col, "text") + "▲")
    else:
        treeview.heading(col, text=treeview.heading(col, "text") + "▼")

    # Reverse the sort order for the next click
    treeview.heading(col, command=lambda: sort_column(treeview, col, not reverse))

# Define light and dark themes
def set_light_theme(root: tk.Tk):
    style = AwthemesStyle(root)
    style.theme_use("awlight")
    root.configure(bg='white')

def set_dark_theme(root: tk.Tk):
    style = AwthemesStyle(root)
    style.theme_use("awdark")
    root.configure(bg='#2e2e2e')

def toggle_theme():
    global dark_mode
    if not dark_mode:
        set_light_theme()
    else:
        set_dark_theme()
    dark_mode = not dark_mode


def create_tree(root):
    global treeview

    # Create a Treeview widget for the table
    treeview = ttk.Treeview(root)

    # Add data to the table
    data = databaseManager.getAllTypesAsList()

    # Create a dictionary to store parent-child relationships
    nodes = {}

    # First, organize the data into parent-child relationships
    for name, parent in data:
        if parent not in nodes:
            nodes[parent] = []
        nodes[parent].append(name)

    extra_node_id = treeview.insert("", 'end', text="Alle Einträge")

    # Recursive function to insert nodes into the Treeview
    def insert_nodes(parent, parent_id=""):
        if parent not in nodes:
            return
        for child in nodes[parent]:
            # Insert the child node under the parent; root nodes have parent_id=""
            child_id = treeview.insert(parent_id, 'end', text=child)
            # Recursively insert its children
            insert_nodes(child, child_id)

    # Insert the root nodes (those with None as parent)
    insert_nodes(None)

    # Place the table in the grid
    treeview.grid(row=0, column=0, padx=20, pady=40, rowspan=5, sticky="nsew")
    treeview.bind("<<TreeviewSelect>>", on_select)

# Function to handle selection
def on_select(event):
    # Get the selected item
    selected_item = treeview.focus()
    # Get item details (e.g., text of the selected item)
    item_text = treeview.item(selected_item, 'text')
    # Update right Table on the GUI with the selected Category
    if item_text == "Alle Einträge":
        table.gui.update_table(databaseManager.getAllRowsAsList())
    else:
        table.gui.update_table(databaseManager.getAllRowsByTypeAsList(item_text))