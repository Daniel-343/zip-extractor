import tkinter as tk
from tkinter import ttk
import psycopg2
from tkinter import messagebox


class UserList(tk.Frame):
    def __init__(self, controller, sql_controller):
        tk.Frame.__init__(self)
        self.controller = controller
        self.SqlController = sql_controller

        self.tree = ttk.Treeview(self, columns=('Name', 'Password', 'Company', 'Customer code', 'Type'),
                                 show='headings')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Password', text='Password')
        self.tree.heading('Company', text='Company')
        self.tree.heading('Customer code', text='Customer code')
        self.tree.heading('Type', text='Type')
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

            users = self.SqlController.get_users()
            rows = [
                {'name': user[0], 'password': user[1], 'company': user[2], 'customer_code': user[3], 'type': user[4]}
                for user in users]

            for row in rows:
                self.tree.insert('', 'end', values=(
                row['name'], row['password'], row['company'], row['customer_code'], row['type']))

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
