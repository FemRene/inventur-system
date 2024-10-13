import databaseManager
import table.gui
from tkinter import ttk

treeview: ttk.Treeview


def create_tree(root):
    global treeview

    # Create a Treeview widget for the table
    treeview = ttk.Treeview(root)

    # Add data to the table
    data = databaseManager.getAllTypesAsList()

    # Create a dictionary to store parent_category-child relationships
    nodes = {}

    # First, organize the data into parent_category-child relationships
    for name, parent in data:
        if parent not in nodes:
            nodes[parent] = []
        nodes[parent].append(name)

    # Recursive function to insert nodes into the Treeview
    def insert_nodes(parent_category, parent_id=""):
        if parent_category not in nodes:
            return
        for child in nodes[parent_category]:
            # Insert the child node under the parent_category; root nodes have parent_id=""
            child_id = treeview.insert(parent_id, 'end', text=child)
            # Recursively insert its children
            insert_nodes(child, child_id)

    # Insert the root nodes (those with None as parent_category)
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
