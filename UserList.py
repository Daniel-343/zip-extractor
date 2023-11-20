import tkinter as tk
from tkinter import ttk
import psycopg2
from tkinter import messagebox


class UserList(tk.Frame):
    def __init__(self, controller, sql_controller):
        tk.Frame.__init__(self)
        self.controller = controller
        self.SqlController = sql_controller

        # Database connection parameters
        self.db_params = {
            'host': 'localhost',
            'database': 'zipdb',
            'user': 'daniel',
            'password': '1324'
        }

        # Create a treeview to display user data
        self.tree = ttk.Treeview(self, columns=('Name', 'Password'), show='headings')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Password', text='Password')
        self.tree.grid(row=0, column=0, columnspan=2, sticky=tk.W + tk.E)

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.scrollbar.grid(row=0, column=1, sticky='nsew')
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        refresh_button = tk.Button(self, text="Refresh", command=self.fetch_users)
        refresh_button.grid(row=2, column=0, columnspan=2, pady=10, sticky=tk.W + tk.E)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        delete_button = tk.Button(self, text="Delete Company", command=self.confirm_delete_user)
        delete_button.grid(row=3, column=0, columnspan=2, pady=10, sticky=tk.W + tk.E)
        self.fetch_users()

    def show(self):
        self.lift()

    def fetch_users(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            connection = psycopg2.connect(**self.db_params)

            cursor = connection.cursor()

            cursor.execute("SELECT name, password FROM \"user\";")

            rows = cursor.fetchall()

            for row in rows:
                self.tree.insert('', 'end', values=row)

            cursor.close()
            connection.close()

        except psycopg2.Error as e:
            tk.messagebox.showerror("Error", f"Database error: {e}")

    def confirm_delete_user(self):
        selected_item = self.tree.selection()
        if not selected_item:
            tk.messagebox.showinfo("Info", "Please select a company to delete.")
            return

        user_name = self.tree.item(selected_item, 'values')[0]

        confirmation = tk.messagebox.askyesno("Confirmation", f"Do you want to delete the company '{user_name}'?")
        if confirmation:
            self.delete_user(user_name)

    def delete_user(self, user_name):
        selected_item = self.tree.selection()
        if not selected_item:
            tk.messagebox.showinfo("Info", "Please select a company to delete.")
            return

        try:
            self.SqlController.delete_user(user_name)

            tk.messagebox.showinfo("Info", f"company '{user_name}' deleted successfully.")
            self.fetch_users()

        except psycopg2.Error as e:
            tk.messagebox.showerror("Error", f"Database error: {e}")
