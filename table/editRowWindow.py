import tkinter as tk
from tkinter.ttk import Treeview, Combobox
from tkinter import ttk

import databaseManager


def openWindow(table: Treeview):
    all_items = table.get_children()
    ids = [table.item(item, "values")[0] for item in all_items]

    root = tk.Tk()
    root.title("Edit Entry")
    root.minsize(200, 300)

    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # ID Label and Entry
    label = tk.Label(frame, text="ID")
    label.pack
    entry_id = ttk.Combobox(frame, values=ids)
    entry_id.set("1")
    entry_id.pack(fill="x", padx=10)

    # ServiceTag Label and Entry
    label = tk.Label(frame, text="ServiceTag")
    label.pack(pady=10)
    entry_service_tag = tk.Entry(frame)
    entry_service_tag.pack(fill="x", padx=10)

    # Type Label and Entry
    label = tk.Label(frame, text="Type")
    label.pack(pady=10)
    entry_type = ttk.Combobox(frame, values=databaseManager.getAllTypesForBoxAsList())
    entry_type.set("Select Type")
    entry_type.pack(fill="x", padx=10)

    # Raum Label and Entry
    label = tk.Label(frame, text="Raum")
    label.pack(pady=10)
    entry_raum = tk.Entry(frame)
    entry_raum.pack(fill="x", padx=10)

    # Add save Button
    save = tk.Button(root, text="Save", command=lambda: saveEdits(root,entry_id,table,entry_service_tag.get(),entry_type.get(),entry_raum.get()))
    save.pack(side="left", padx=5)

    # Add cancel Button
    save = tk.Button(root, text="Cancel", command=lambda: root.destroy())
    save.pack(side="right", padx=5)

    # Run the Tkinter event loop
    on_combobox_select(entry_id, table, entry_service_tag, entry_type, entry_raum)
    entry_id.bind("<<ComboboxSelected>>", lambda event: on_combobox_select(entry_id, table, entry_service_tag, entry_type, entry_raum))
    root.mainloop()

def on_combobox_select(box: Combobox, table: Treeview, service, typ, raum):
    selected_value = box.get()
    all_items = table.get_children()
    for item in all_items:
        item_id = table.item(item, "values")[0]
        if item_id == selected_value:
            row_values = table.item(item, "values")
            service.delete(0, tk.END)
            service.insert(0, row_values[1])
            typ.delete(0, tk.END)
            typ.insert(0, row_values[2])
            raum.delete(0, tk.END)
            raum.insert(0, row_values[3])

def saveEdits(window: tk.Tk, box: Combobox, table: Treeview, service, typ, raum):
    selected_value = box.get()
    all_items = table.get_children()
    for item in all_items:
        item_id = table.item(item, "values")[0]
        if item_id == selected_value:
            table.delete(item)
            table.insert("", tk.END, values=(selected_value, service, typ, raum))
            databaseManager.updateRow(selected_value,service,typ,raum)
            window.destroy()