# this for contains all the student information

from tkinter import *
from tkinter.ttk import Treeview
import Database.database


class ViewFacultyDetailsWindow:

    def __init__(self):
        self.win = Tk()
        self.canvas = Canvas(self.win, width=900, height=450, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 900 / 2)
        y = int(height / 2 - 450 / 2)
        str1 = "900x450+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        # disable resize window
        self.win.resizable(False, False)

        # changing title of the window
        self.win.title("| VIEWING FACULTY DETAILS | LIBRARY MANAGEMENT SYSTEM |")

    def add_frame(self):
        self.frame = Frame(self.win, height=450, width=900)
        self.frame.place(x=0, y=0)

        x, y = 0, 0

        self.label = Label(self.frame, text="VIEW FACULTY DETAILS", fg='black')
        self.label.config(font=("Poppins", 20, 'underline bold'))
        self.label.place(x=265, y=30)

        # use tree view to show details from the table
        self.tr = Treeview(self.frame, columns=('A', 'B', 'C', 'D'), selectmode="extended")
        # heading key + text
        # self.tr.heading('#0', text='S/L NO')
        # self.tr.column('#0', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#0', text='STUDENT_ID')
        self.tr.column('#0', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#1', text='FULL_NAME')
        self.tr.column('#1', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#2', text='GENDER')
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#3', text='DEPARTMENT')
        self.tr.column('#3', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#4', text='CONTACT NO')
        self.tr.column('#4', minwidth=0, width=100, stretch=NO)
        # self.tr.heading('#7', text='Update')
        # self.tr.column('#7', minwidth=0, width=80, stretch=NO)
        # self.tr.heading('#8', text='Delete')
        # self.tr.column('#8', minwidth=0, width=80, stretch=NO)

        j = 0
        for i in Database.database.Faculties():
            self.tr.insert('', index=j, text=i[0], values=(i[1], i[2], i[3], i[4]))
            j += 1

        self.tr.place(x=200, y=y + 100)

        self.win.mainloop()
