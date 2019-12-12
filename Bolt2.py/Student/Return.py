# this page contains student who taken books from library.. and also it shows issue date and return date

from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import Database.database
import Student
import Thirdpage


class ReturnWindow:

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
        self.win.title("| BOOK RETURNING DETAILS | LIBRARY MANAGEMENT SYSTEM |")

    def add_frame(self):

        self.frame = Frame(self.win, height=420, width=800)
        self.frame.place(x=0, y=0)

        x, y = 0, 0

        self.label = Label(self.frame, text="BOOK RETURNING BY STUDENT", fg='black')
        self.label.config(font=("Poppins", 20, 'underline bold'))
        self.label.place(x=175, y=30)

        # use tree view to show details from the table
        self.tr = Treeview(self.frame, columns=('BOOK_ID', 'STUDENT_ID', 'ISSUE_DATE', 'RETURN_DATE'),
                           selectmode="extended")

        self.tr.heading('#0', text='BOOK_ID')
        self.tr.column('#0', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#1', text='STUDENT_ID')
        self.tr.column('#1', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#2', text='ISSUE_DATE')
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#3', text='RETURN_DATE')
        self.tr.column('#3', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#4', text='RETURN')
        self.tr.column('#4', minwidth=0, width=100, stretch=NO)
        # self.tr.heading('#5', text='RETURN')
        # self.tr.column('#5', minwidth=0, width=100, stretch=NO)

        j = 0
        for i in Database.database.BookLend():
            self.tr.insert('', index=j, text=i[0], values=(i[1], i[2], i[3], 'RETURN'))
            j += 1

        # create action on deletion
        self.tr.bind('<Double-Button-1>', self.bounce)
        self.tr.place(x=140, y=y + 100)

        self.win.mainloop()

    def bounce(self, e):
        # get the value of deleted row
        tt = self.tr.focus()
        # get the column id
        col = self.tr.identify_column(e.x)
        # print(col)
        # print(self.tr.item(tt))
        # print(self.tr.item(tt)['text'])
        # print(self.tr.item(tt)['values'][0])
        data = (
            str(self.tr.item(tt)['text']),
            str(self.tr.item(tt)['values'][0]),
        )

        if col == '#4':
            res = messagebox.askyesno("Message", "Do you want  to Return..!")
            if res:
                d, fine_days = Database.database.Return(data)
                if d:
                    message = ("Book Returned successfully..! \n Fine = ", fine_days)
                    messagebox.showinfo("Message", message)
                    self.win.destroy()
                    x = Thirdpage
            else:
                self.win.destroy()
                x = Student.Return.ReturnWindow()
                x.add_frame()
