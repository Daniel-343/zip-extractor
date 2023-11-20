import tkinter as tk
import psycopg2
from tkinter import messagebox


class AddUser(tk.Frame):
    def __init__(self, controller, sql_controller):
        tk.Frame.__init__(self)
        self.controller = controller
        self.sqlController = sql_controller

        self.name_entry = tk.Entry(self, width=30)
        self.password_entry = tk.Entry(self, width=30)

        tk.Label(self, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        self.password_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        add_button = tk.Button(self, text="Add Company", command=self.add_user)
        add_button.grid(row=2, column=0, columnspan=2, pady=10)

    def show(self):
        self.lift()

    def add_user(self):
        name = self.name_entry.get()
        password = self.password_entry.get()

        if not name or not password:
            tk.messagebox.showinfo("Info", "Please enter both name and password.")
            return

        try:
            self.sqlController.add_user(name, password)

            tk.messagebox.showinfo("Info", f"Company '{name}' added successfully.")

        except psycopg2.Error as e:
            tk.messagebox.showerror("Error", f"Database error: {e}")
