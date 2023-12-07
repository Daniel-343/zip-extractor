import tkinter as tk
import psycopg2
from tkinter import messagebox


class AddUser(tk.Frame):
    def __init__(self, controller, sql_controller, user_list):
        tk.Frame.__init__(self)
        self.userList = user_list
        self.button_check_0 = tk.IntVar()
        self.button_check_1 = tk.IntVar()
        self.type_entry = None
        self.controller = controller
        self.sqlController = sql_controller

        self.name_entry = tk.Entry(self, width=30)
        self.password_entry = tk.Entry(self, width=30)
        self.company_entry = tk.Entry(self, width=30)
        self.customer_code_entry = tk.Entry(self, width=30)

        tk.Label(self, text="Name*:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="Password*:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="Company:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="Customer code*:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="Type*:").grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        self.password_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
        self.company_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
        self.customer_code_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

        self.name_entry1 = tk.Entry(self, width=30)
        self.password_entry1 = tk.Entry(self, width=30)
        self.company_entry1 = tk.Entry(self, width=30)
        self.customer_code_entry1 = tk.Entry(self, width=30)

        tk.Label(self, text="Name*:").grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="Password*:").grid(row=1, column=2, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="Company:").grid(row=2, column=2, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="Customer code*:").grid(row=3, column=2, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="Type*:").grid(row=4, column=2, padx=10, pady=5, sticky=tk.W)

        self.name_entry1.grid(row=0, column=3, padx=10, pady=5, sticky=tk.W)
        self.password_entry1.grid(row=1, column=3, padx=10, pady=5, sticky=tk.W)
        self.company_entry1.grid(row=2, column=3, padx=10, pady=5, sticky=tk.W)
        self.customer_code_entry1.grid(row=3, column=3, padx=10, pady=5, sticky=tk.W)

        company_button = tk.Checkbutton(self, text="Company", command=lambda: self.toggle_type(0),
                                        variable=self.button_check_0)
        company_button.grid(row=4, column=0, columnspan=2, padx=(0, 40), pady=10)

        person_button = tk.Checkbutton(self, text="Person", command=lambda: self.toggle_type(1),
                                       variable=self.button_check_1)
        person_button.grid(row=4, column=1, columnspan=2, pady=10)

        add_button = tk.Button(self, text="Add Company", command=self.add_user)
        add_button.grid(row=5, column=0, columnspan=2, pady=10)

    def show(self):
        self.lift()

    def add_user(self):
        name = self.name_entry.get()
        password = self.password_entry.get()
        company = self.company_entry.get()
        customer_number = self.customer_code_entry.get()
        entry_type = self.type_entry

        if not name or not password or not customer_number or not entry_type:
            tk.messagebox.showinfo("Info", "Please enter all required fields")
            return

        try:
            self.sqlController.add_user(name, password, company, customer_number, entry_type)
            self.clear_entries()
            self.userList.fetch_users()
            tk.messagebox.showinfo("Info", f"'{name}' added successfully.")

        except psycopg2.Error as e:
            tk.messagebox.showerror("Error", f"Database error: {e}")

    def toggle_type(self, button_index):

        if button_index == 0:
            self.type_entry = 'company'
            self.button_check_0.set(1)
            self.button_check_1.set(0)
        elif button_index == 1:
            self.type_entry = 'person'
            self.button_check_0.set(0)
            self.button_check_1.set(1)


    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.company_entry.delete(0, tk.END)
        self.customer_code_entry.delete(0, tk.END)
        self.type_entry = None
        self.button_check_0 = 0
        self.button_check_1 = 0

