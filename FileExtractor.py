import os
import tkinter as tk
import zipfile
from tkinter import filedialog, messagebox


def show_popup(message):
    messagebox.showinfo("File Extractor", message)


class FileExtractorApp(tk.Frame):
    def __init__(self, sql_controller):
        tk.Frame.__init__(self)

        self.SqlController = sql_controller
        self.file_path = tk.StringVar()

        self.entry_prompt = tk.Label(self, text='Choose file to extract')
        self.entry_prompt.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.file_path_entry = tk.Entry(self, textvariable=self.file_path, width=50)
        self.file_path_entry.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        self.browse_button = tk.Button(self, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=2, column=0, padx=10, pady=10)

        self.extract_button = tk.Button(self, text="Extract", command=self.find_password)
        self.extract_button.grid(row=2, column=1, padx=10, pady=10)

    def show(self):
        self.lift()

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Zip files", "*.zip"), ("All files", "*.*")])
        self.file_path.set(file_path)

    def extract_file(self, password):
        output_folder = os.path.dirname(self.file_path.get())
        try:
            with zipfile.ZipFile(self.file_path.get(), 'r') as zip_ref:
                zip_ref.extractall(output_folder, pwd=password.encode('utf-8'))
            show_popup('File extraction successful')
            return True
        except zipfile.BadZipFile:
            show_popup("Error: The file is not a valid zip file.")
        except zipfile.LargeZipFile:
            show_popup("Error: The zip file is too large to handle.")
        except RuntimeError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

        return False

    def find_password(self):
        users = self.SqlController.get_users()
        for entry in users:
            if self.extract_file(entry['password']):
                break
