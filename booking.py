import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from database import create_reservation

def open_booking_window(parent):
    booking_win = tk.Toplevel(parent)
    booking_win.title("Book a Flight")
    booking_win.geometry("400x400")

    fields = {}

    labels = [
        "Name", "Flight Number", "Departure", "Destination", "Date (YYYY-MM-DD)", "Seat Number"
    ]

    for i, label_text in enumerate(labels):
        label = tk.Label(booking_win, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=5, sticky='w')

        entry = tk.Entry(booking_win, width=30)
        entry.grid(row=i, column=1, padx=10, pady=5)
        fields[label_text] = entry

    def submit():
        name = fields["Name"].get()
        flight_number = fields["Flight Number"].get()
        departure = fields["Departure"].get()
        destination = fields["Destination"].get()
        date = fields["Date (YYYY-MM-DD)"].get()
        seat_number = fields["Seat Number"].get()

        # Simple date validation
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Invalid Date", "Date must be in YYYY-MM-DD format.")
            return

        if not all([name, flight_number, departure, destination, date, seat_number]):
            messagebox.showwarning("Missing Fields", "All fields are required.")
            return

        # For now just print to console
        create_reservation(name, flight_number, departure, destination, date, seat_number)
        messagebox.showinfo("Success", "Reservation saved successfully.")
        booking_win.destroy()

    submit_btn = tk.Button(booking_win, text="Submit", command=submit)
    submit_btn.grid(row=len(labels), column=0, columnspan=2, pady=20)
