# reservations.py
import tkinter as tk
from tkinter import ttk, messagebox
from database import fetch_all_reservations, delete_reservation
from edit_reservation import open_edit_window

def open_reservations_window(parent):
    win = tk.Toplevel(parent)
    win.title("All Reservations")
    win.geometry("700x400")

    columns = ("id", "name", "flight", "from", "to", "date", "seat")
    tree = ttk.Treeview(win, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col.capitalize())
        tree.column(col, anchor="center")

    tree.pack(expand=True, fill="both", padx=10, pady=10)

    def refresh_table():
        # Clear table
        for item in tree.get_children():
            tree.delete(item)
        # Re-fetch from DB
        reservations = fetch_all_reservations()
        for row in reservations:
            tree.insert("", "end", values=row)

    def edit_selected():
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showwarning("No Selection", "Select a reservation first.")
            return

        data = tree.item(selected_item)['values']
        if not data:
            messagebox.showerror("Error", "Unable to read selected data.")
            return

        open_edit_window(win, data, refresh_table)  # pass refresh as callback

    def delete_selected():
        selected_items = tree.selection()
        if not selected_items:
            messagebox.showwarning("No Selection", "Select a reservation first.")
            return

        selected_item = selected_items[0]
        data = tree.item(selected_item)['values']
        data = tree.item(selected_item)['values']
        res_id = data[0]
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete reservation ID {res_id}?")
        if confirm:
            delete_reservation(res_id)
            refresh_table()
            messagebox.showinfo("Deleted", "Reservation deleted.")

    # Buttons
    btn_frame = tk.Frame(win)
    btn_frame.pack(pady=10)

    edit_btn = tk.Button(btn_frame, text="Edit Selected", command=edit_selected)
    edit_btn.pack(side="left", padx=5)

    refresh_btn = tk.Button(btn_frame, text="Refresh", command=refresh_table)
    refresh_btn.pack(side="left", padx=5)

    refresh_table()  # Load data on first open

    # Delete Reservation Button
    delete_btn = tk.Button(btn_frame, text="Delete Reservation", width=20, command=delete_selected)
    delete_btn.pack(side="left", padx=5)