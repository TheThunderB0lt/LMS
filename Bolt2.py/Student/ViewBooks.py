# this for contains all the Book information

from tkinter import *
import tkinter as tk
from tkinter.ttk import Treeview
import Database.database


class ViewBookWindow:

    def __init__(self):
        self.win = tk.Tk()
        self.canvas = Canvas(self.win, width=800, height=450, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 800 / 2)
        y = int(height / 2 - 450 / 2)
        str1 = "800x450+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        # disable resize window
        self.win.resizable(False, False)

        # changing title of the window
        self.win.title("| VIEWING BOOK DETAILS | LIBRARY MANAGEMENT SYSTEM |")

    def add_frame(self):
        self.frame = Frame(self.win, height=450, width=800)
        self.frame.place(x=0, y=0)

        # x, y = 0, 0

        self.label = Label(self.frame, text="VIEW BOOK DETAILS", fg='black')
        self.label.config(font=("Poppins", 20, 'underline bold'))
        self.label.place(x=265, y=30)

        # use tree view to show details from the table
        self.tr = Treeview(self.frame, columns=('A', 'B', 'C', 'D', 'E'), selectmode="extended")

        # heading key + text
        self.tr.heading('#0', text='BOOK_ID')
        self.tr.column('#0', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#1', text='BOOK_TITLE')
        self.tr.column('#1', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#2', text='AUTHOR NAME')
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#3', text='PUBLISHED_YEAR')
        self.tr.column('#3', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#4', text='PRICE')
        self.tr.column('#4', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#5', text='BOOK_CATEGORY')
        self.tr.column('#5', minwidth=0, width=115, stretch=NO)

        self.list = ['None', 'First Sem', 'Second Sem', 'Third Sem', 'Fourth Sem', 'Fifth Sem', 'Sixth Sem',
                     'Seventh Sem', 'Eighth Sem', 'Management', 'Technology', 'News paper', 'Magazines']
        self.filter = tk.StringVar(self.frame)
        self.drop = tk.OptionMenu(self.frame, self.filter, *self.list)
        self.drop.config(width=24)
        self.filter.set(self.list[0])
        self.drop.place(x=440, y=94)
        # self.filter = Entry(self.frame, font="Arial 12")
        # self.filter.place(x=440, y=94)
        search_text = self.filter.get()
        self.btn = Button(self.frame, text='SEARCH', width=9, bg='white', fg='black', font=("Poppins", 11, "bold"),
                          command=self.sea)
        self.btn.place(x=630, y=90)
        j = 0

        for i in Database.database.ViewBooks():
            self.tr.insert('', index=j, text=i[0], values=(i[1], i[2], i[3], i[4], i[5]))
            j += 1
        self.tr.place(x=100, y=140)

    def sea(self):
        nk = (
            self.filter.get(),
        )
        self.tr = Treeview(self.frame, columns=('A', 'B', 'C', 'D', 'E'), selectmode="extended")
        print(nk)

        # heading key + text
        self.tr.heading('#0', text='BOOK_ID')
        self.tr.column('#0', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#1', text='BOOK_TITLE')
        self.tr.column('#1', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#2', text='AUTHOR NAME')
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#3', text='PUBLISHED_YEAR')
        self.tr.column('#3', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#4', text='PRICE')
        self.tr.column('#4', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#5', text='BOOK_CATEGORY')
        self.tr.column('#5', minwidth=0, width=115, stretch=NO)

        j = 0
        if nk[0] == "":
            for i in Database.database.ViewBooks():
                self.tr.insert('', index=j, text=i[0], values=(i[1], i[2], i[3], i[4], i[5]))
                j += 1
        else:
            for i in Database.database.filter(nk):
                self.tr.insert('', index=j, text=i[0], values=(i[1], i[2], i[3], i[4], i[5]))
                j += 1

        self.tr.place(x=100, y=140)
        self.win.mainloop()
