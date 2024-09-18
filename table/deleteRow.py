from tkinter.ttk import Treeview

import databaseManager


def deleteSelectedRow(table: Treeview):
    selected_item = table.selection()
    if selected_item:
        item_id = selected_item[0]
        item_data = table.item(item_id)
        values = item_data['values']
        if values:
            first_column_value = values[0]
            table.delete(table.focus())
            databaseManager.deleteRowByID(first_column_value)