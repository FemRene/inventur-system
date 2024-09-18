from tkinter.ttk import Treeview

def deleteSelectedRow(table: Treeview):
    if table.selection():
        table.delete(table.focus())