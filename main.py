# main.py
import tkinter as tk
from home import HomePage

def main():
    root = tk.Tk()
    root.title("Flight Reservation System")
    root.geometry("400x300")

    home_page = HomePage(root, root)
    home_page.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
