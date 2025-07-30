# database.py
import sqlite3
import os
import sys
import shutil

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def get_writable_db_path():
    # Always use ./data/flights.db at runtime
    local_dir = os.path.join(os.getcwd(), "data")
    os.makedirs(local_dir, exist_ok=True)
    local_db = os.path.join(local_dir, "flights.db")

    # If it doesn't exist yet, copy from bundled version
    if not os.path.exists(local_db):
        bundled_db = resource_path("flights.db")
        shutil.copyfile(bundled_db, local_db)

    return local_db

def connect():
    db_path = get_writable_db_path()
    return sqlite3.connect(db_path)

def fetch_all_reservations():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM reservations")
    rows = cur.fetchall()
    conn.close()
    return rows

def create_reservation(name, flight_number, departure, destination, date, seat_number):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, flight_number, departure, destination, date, seat_number))
    conn.commit()
    conn.close()

def update_reservation(res_id, name, flight_number, departure, destination, date, seat_number):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        UPDATE reservations
        SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
        WHERE id = ?
    """, (name, flight_number, departure, destination, date, seat_number, res_id))
    conn.commit()
    conn.close()

def delete_reservation(res_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM reservations WHERE id = ?", (res_id,))
    conn.commit()
    conn.close()