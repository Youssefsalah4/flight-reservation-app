# edit_reservation.py
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from database import update_reservation

def open_edit_window(parent, data, on_update_callback):
    edit_win = tk.Toplevel(parent)
    edit_win.title("Edit Reservation")
    edit_win.geometry("400x400")

    res_id, name, flight_number, departure, destination, date, seat_number = data

    fields = {}

    labels = [
        "Name", "Flight Number", "Departure", "Destination", "Date (YYYY-MM-DD)", "Seat Number"
    ]

    values = [name, flight_number, departure, destination, date, seat_number]

    for i, (label_text, value) in enumerate(zip(labels, values)):
        label = tk.Label(edit_win, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=5, sticky='w')

        entry = tk.Entry(edit_win, width=30)
        entry.insert(0, value)
        entry.grid(row=i, column=1, padx=10, pady=5)
        fields[label_text] = entry

    def update():
        name = fields["Name"].get()
        flight_number = fields["Flight Number"].get()
        departure = fields["Departure"].get()
        destination = fields["Destination"].get()
        date = fields["Date (YYYY-MM-DD)"].get()
        seat_number = fields["Seat Number"].get()

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Invalid Date", "Date must be in YYYY-MM-DD format.")
            return

        if not all([name, flight_number, departure, destination, date, seat_number]):
            messagebox.showwarning("Missing Fields", "All fields are required.")
            return

        update_reservation(res_id, name, flight_number, departure, destination, date, seat_number)
        messagebox.showinfo("Success", "Reservation updated successfully.")
        edit_win.destroy()
        on_update_callback()

    update_btn = tk.Button(edit_win, text="Update", command=update)
    update_btn.grid(row=len(labels), column=0, columnspan=2, pady=20)
