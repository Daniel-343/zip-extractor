import os
import tkinter as tk
import psycopg2
from tkinter import messagebox


class SettingsPage(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.ip_entry = tk.Entry(self, width=30)
        self.port_entry = tk.Entry(self, width=30)

        tk.Label(self, text="Database settings").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="IP address:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="Port:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        self.ip_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
        self.ip_entry.insert(0, os.getenv("HOST"))
        self.port_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
        self.port_entry.insert(0, os.getenv("PORT"))

        save_button = tk.Button(self, text="Save", command=self.saveSettings)
        save_button.grid(row=5, column=0, columnspan=2, pady=10)

    def show(self):
        self.lift()

    def saveSettings(self):
        host = self.ip_entry.get()
        port = self.port_entry.get()

        if not self.ip_entry.get() or not self.port_entry.get():
            tk.messagebox.showinfo("Info", "Please enter all required fields")
            return

        try:
            with open('.env', 'r') as f:
                lines = f.readlines()

            updated_lines = []
            for line in lines:
                if line.startswith("HOST="):
                    updated_lines.append(f"HOST={host}\n")
                elif line.startswith("PORT="):
                    updated_lines.append(f"PORT={port}\n")
                else:
                    updated_lines.append(line)

            with open('.env', 'w') as f:
                f.writelines(updated_lines)
            tk.messagebox.showinfo("Info", f"Settings saved successfully.")

        except Exception as e:
            tk.messagebox.showerror("Error", f"D error: {e}")
