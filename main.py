import tkinter as tk
from FileExtractor import FileExtractorApp
from UserList import UserList
from AddUserFrame import AddUser
from SqlController import SqlController


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.sql_controller = SqlController()
        p1 = UserList(self, self.sql_controller)
        p2 = FileExtractorApp(self.sql_controller)
        p3 = AddUser(self, self.sql_controller, p1)

        button_frame = tk.Frame(self)
        container = tk.Frame(self)
        button_frame.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(button_frame, text="Database", command=p1.show)
        b2 = tk.Button(button_frame, text="Extract", command=p2.show)
        b3 = tk.Button(button_frame, text="Add New", command=p3.show)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

    def run(self, root_display):
        root_display.title("Zip Extractor")
        width = root_display.winfo_screenwidth()
        height = root_display.winfo_screenheight()
        root_display.geometry("%dx%d" % (width, height))
        self.pack(side="top", fill="both", expand=True)
        root_display.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainView(root)
    app.run(root)
