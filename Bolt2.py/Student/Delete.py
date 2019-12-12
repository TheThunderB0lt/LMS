# this for contains all the Book information only the admin can delete..

from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import Database.database
import Student.AddBook
import Thirdpage


class DeleteWindow:

    def __init__(self, data=''):
        self.data = data
        print(self.data)
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
        self.win.title("| DELETING BOOK DETAILS | LIBRARY MANAGEMENT SYSTEM |")

    def add_frame(self):

        self.frame = Frame(self.win, height=420, width=800)
        self.frame.place(x=0, y=0)

        x, y = 0, 0

        self.label = Label(self.frame, text="DELETING BOOK DETAILS", fg='black')
        self.label.config(font=("Poppins", 20, 'underline bold'))
        self.label.place(x=235, y=35)

        # use tree view to show details from the table
        self.tr = Treeview(self.frame, columns=('BOOK_ID', 'BOOK_TITLE', 'AUTHOR_NAME', 'PUBLISHED_YEAR', 'PRICE'),
                           selectmode="extended")

        # heading key + text

        self.tr.heading('#0', text='BOOK_ID')
        self.tr.column('#0', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#1', text='BOOK_TITLE')
        self.tr.column('#1', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#2', text='AUTHOR_NAME')
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#3', text='PUBLISHED_YEAR')
        self.tr.column('#3', minwidth=0, width=110, stretch=NO)
        self.tr.heading('#4', text='PRICE')
        self.tr.column('#4', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#5', text='DELETE')
        self.tr.column('#5', minwidth=0, width=100, stretch=NO)
        # self.tr.heading('#6', text='DELETE')
        # self.tr.column('#6', minwidth=0, width=100, stretch=NO)

        j = 0
        for i in Database.database.ViewBooks():
            self.tr.insert('', index=j, text=i[0], values=(i[1], i[2], i[3], i[4], 'DELETE'))
            j += 1

        # create action on deletion
        self.tr.bind('<Double-Button-1>', self.actions)
        self.tr.place(x=100, y=y + 100)

        self.win.mainloop()

    def actions(self, e):
        # get the value of deleted row
        tt = self.tr.focus()

        # get the column id
        col = self.tr.identify_column(e.x)
        print(col)
        print(self.tr.item(tt))

        data = (
            self.tr.item(tt).get('text'),
        )

        if col == '#5':
            res = messagebox.askyesno("Message", "Do you want  to delete..!")
            if res:
                d = Database.database.Delete(data)
                if d:
                    messagebox.showinfo("Message", "Book Details deleted successfully..!")
                    self.win.destroy()
                    x = Thirdpage
            else:
                self.win.destroy()
                x = Student.Delete.DeleteWindow()
                x.add_frame()

        # elif col == '#5':
        #     res = messagebox.askyesno("Message", "Do you want  to update..!")
        #     if res:
        #         res = Student.AddBook.BooksWindow(self.tr.item(tt))
        #         self.win.destroy()
        #         res.add_frame()
