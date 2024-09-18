import tkinter as tk
from tkinter.ttk import Treeview
from tkinter import ttk

def openWindow(table: Treeview):
    # Get all entries from the table and find the highest ID
    all_items = table.get_children()
    ids = [int(table.item(item, "values")[0]) for item in all_items]
    highest_id = max(ids) if ids else 0

    # Create a new Tkinter window
    root = tk.Tk()
    root.title("Add a new Entry")
    root.minsize(200, 300)

    # Create a frame for better layout control
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # ID Label and Entry
    label = tk.Label(frame, text="ID")
    label.pack(pady=10)
    entry_id = tk.Entry(frame)
    entry_id.insert(0, str(highest_id + 1))
    entry_id.config(state="disabled")
    entry_id.pack(fill="x", padx=10)

    # ServiceTag Label and Entry
    label = tk.Label(frame, text="ServiceTag")
    label.pack(pady=10)
    entry_service_tag = tk.Entry(frame)
    entry_service_tag.pack(fill="x", padx=10)

    # Type Label and Entry
    label = tk.Label(frame, text="Type")
    label.pack(pady=10)
    entry_type = ttk.Combobox(frame, values=["PC", "Bildschirm", "Laptop", "Buch", "Stift"])
    entry_type.set("Select Type")
    entry_type.pack(fill="x", padx=10)

    # Raum Label and Entry
    label = tk.Label(frame, text="Raum")
    label.pack(pady=10)
    entry_raum = tk.Entry(frame)
    entry_raum.pack(fill="x", padx=10)

    # Add save Button
    save = tk.Button(root, text="Save", command=lambda: addToTree(root, table, entry_id.get(), entry_service_tag.get(), entry_type.get(), entry_raum.get()))
    save.pack(side="left", padx=5)

    # Add cancel Button
    save = tk.Button(root, text="Cancel", command=lambda: root.destroy())
    save.pack(side="right", padx=5)

    # Run the Tkinter event loop
    root.mainloop()

def addToTree(window: tk.Tk, table: Treeview, id, serviceTag, typ, raum):
    table.insert("", tk.END, values=(id, serviceTag, typ, raum))
    window.destroy()