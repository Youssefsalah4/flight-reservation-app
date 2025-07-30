# home.py
import tkinter as tk
from booking import open_booking_window
from reservations import open_reservations_window

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        title_label = tk.Label(self, text="Welcome to Flight Reservation", font=("Helvetica", 16))
        title_label.pack(pady=30)

        book_btn = tk.Button(self, text="Book Flight", width=20,
                             command=lambda: open_booking_window(self))
        book_btn.pack(pady=10)

        view_btn = tk.Button(self, text="View Reservations", width=20,
                             command=lambda: open_reservations_window(self))
        view_btn.pack(pady=10)
