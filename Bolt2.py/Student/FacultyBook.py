# this is book lending form

from tkinter import *
import tkinter.messagebox as k
import Database.database
import datetime


class FacultyBookWindow:

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
        self.win.title("| FACULTY BOOKS LENDING | LIBRARY MANAGEMENT SYSTEM |")

    def add_frame(self):
        self.frame = Frame(self.win, height=440, width=800)
        self.frame.place(x=0, y=0)

        x, y = 70, 20

        self.label = Label(self.frame, text="FACULTY BOOK LENDING", fg='black')
        self.label.config(font=("Poppins", 20, 'underline bold'))
        self.label.place(x=230, y=40)

        # creating book id label and entry field
        self.label1 = Label(self.frame, text="BOOK ID")
        self.label1.config(font=("Poppins", 14, 'bold'))
        self.label1.place(x=185, y=130)

        self.bid = Entry(self.frame, font="Poppins 11")
        self.bid.place(x=320, y=132)

        # creating book title label and entry field
        self.label2 = Label(self.frame, text="FACULTY ID")
        self.label2.config(font=("Poppins", 14, 'bold'))
        self.label2.place(x=185, y=190)

        self.id = Entry(self.frame, font="Poppins 11")
        self.id.place(x=320, y=192)

        # creating student author name label and entry field
        # self.label3 = Label(self.frame, text="ISSUE DATE")
        # self.label3.config(font=("Times", 14, 'bold'))
        # self.label3.place(x=185, y=200)
        #
        # self.cal = DateEntry(self.win, width=14, day=22, month=6, year=2019, bg='blue', fg='white', bd=4)
        # self.cal.place(x=320, y=202)
        # # self.idt = Entry(self.frame, font="Arial 12")
        # # self.idt.place(x=320, y=202)
        #
        # self.label3 = Label(self.frame, text="RETURN DATE")
        # self.label3.config(font=("Times", 14, 'bold'))
        # self.label3.place(x=170, y=250)
        #
        # self.rcal = DateEntry(self.win, width=14, day=22, month=6, year=2019, bg='blue', fg='white', bd=4)
        # self.rcal.place(x=320, y=252)
        #
        self.btn = Button(self.frame, text='SUBMIT', width=15, bg='light grey', fg='black',
                          font=("Times", 13, "bold"), command=self.FacultyBookLending)
        self.btn.place(x=320, y=250)

        self.win.mainloop()

    def FacultyBookLending(self):
        id = (
            self.id.get(),
            self.id.get(),
        )
        # print(type(id))
        data = (
            self.bid.get(),
            self.id.get(),
            datetime.date.today().strftime("%m/%d/%Y"),
            (datetime.datetime.strptime(str(datetime.date.today().strftime("%m/%d/%Y")),
                                        "%m/%d/%Y")+datetime.timedelta(days=7)).strftime("%m/%d/%Y"),
        )
        print(data)
        # it shows red color message if student id and name is not entered..
        if self.bid.get() == '':
            self.label1.config(fg='red')
            self.label1.config(text="Please enter Book Id", font=('Poppins', 11, 'bold'))

        elif self.id.get() == '':
            self.label2.config(fg='red')
            self.label2.config(text="Please enter Faculty Id", font=('Poppins', 11, 'bold'))

            # it shows error message if student id is same..and database is locked
        else:
            status, id_status = Database.database.FacultyBookLending(data, id)
            if status and id_status:
                k.showinfo("Welcome", "Book given successfully...!")
                self.win.destroy()
            elif status == 1 and id_status == 0:
                k.showinfo("Already 3 Books Issued to this Faculty_id Try to returning a book to borrow another")
                self.win.destroy()
            else:
                k.showinfo("Enter valid details")
