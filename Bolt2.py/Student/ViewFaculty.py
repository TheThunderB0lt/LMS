# this for contains all the Book lending information

from tkinter import *
from tkinter.ttk import Treeview
import Database.database


class FacultyBookLendWindow:

    def __init__(self):
        self.win = Tk()
        self.canvas = Canvas(self.win, width=800, height=420, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 800 / 2)
        y = int(height / 2 - 420 / 2)
        str1 = "800x420+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        # disable resize window
        self.win.resizable(False, False)

        # changing title of the window
        self.win.title("| BOOK LENDING DETAILS | LIBRARY MANAGEMENT SYSTEM |")

    def add_frame(self):
        self.frame = Frame(self.win, height=420, width=800)
        self.frame.place(x=0, y=0)

        x, y = 0, 0

        self.label = Label(self.frame, text="VIEW FACULTY BOOK LENDING", fg='black')
        self.label.config(font=("Poppins", 20, 'underline bold'))
        self.label.place(x=185, y=30)

        # use tree view to show details from the table
        self.tr = Treeview(self.frame, columns=('A', 'B', 'C'), selectmode="extended")

        # heading key + text
        self.tr.heading('#0', text='BOOK_ID')
        self.tr.column('#0', minwidth=0, width=120, stretch=NO)
        self.tr.heading('#1', text='FACULTY_ID')
        self.tr.column('#1', minwidth=0, width=120, stretch=NO)
        self.tr.heading('#2', text='ISSUE_DATE')
        self.tr.column('#2', minwidth=0, width=120, stretch=NO)
        self.tr.heading('#3', text='RETURN_DATE')
        self.tr.column('#3', minwidth=0, width=120, stretch=NO)
        # self.tr.heading('#4', text='FINE')
        # self.tr.column('#4', minwidth=0, width=100, stretch=NO)

        j = 0
        for i in Database.database.FacultyBookLend():
            self.tr.insert('', index=j, text=i[0], values=(i[1], i[2], i[3]))
            j += 1

        self.tr.place(x=155, y=y + 100)

        self.win.mainloop()
