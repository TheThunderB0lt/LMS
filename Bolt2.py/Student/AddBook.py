# this form contains adding new books

from tkinter import *
# from PIL import ImageTk, Image
import tkinter as tk
import tkinter.messagebox as k
import Database.database
# import Student.Delete


class BooksWindow:

    def __init__(self, data=''):

        self.win = tk.Tk()
        self.data = data
        print(self.data)
        self.canvas = Canvas(self.win, width=800, height=460, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 800 / 2)
        y = int(height / 2 - 460 / 2)
        str1 = "800x460+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        # disable resize window
        self.win.resizable(False, False)

        # changing title of the window
        self.win.title("| ADDING BOOKS | LIBRARY MANAGEMENT SYSTEM |")

    def add_frame(self):
        self.frame = Frame(self.win, height=460, width=800)
        self.frame.place(x=0, y=0)

        x, y = 70, 20

        self.label = Label(self.frame, text="ADDING NEW BOOKS", fg='black')
        self.label.config(font=("helvetica", 20, 'underline bold'))
        self.label.place(x=255, y=15)

        # creating book id label and entry field
        self.label1 = Label(self.frame, text="BOOK ID")
        self.label1.config(font=("Times", 14, 'bold'))
        self.label1.place(x=80, y=85)

        self.bid = Entry(self.frame, font="Arial 12")
        self.bid.place(x=265, y=87)

        # creating book title label and entry field
        self.label2 = Label(self.frame, text="BOOK TITLE")
        self.label2.config(font=("Times", 14, 'bold'))
        self.label2.place(x=80, y=125)

        self.bkt = Entry(self.frame, font="Arial 12")
        self.bkt.place(x=265, y=127)

        # creating author name label and entry field
        self.label3 = Label(self.frame, text="AUTHOR NAME")
        self.label3.config(font=("Times", 14, 'bold'))
        self.label3.place(x=80, y=165)

        self.aut = Entry(self.frame, font="Arial 12")
        self.aut.place(x=265, y=167)

        # creating published year label and entry field
        self.label4 = Label(self.frame, text="PUBLISHED YEAR")
        self.label4.config(font=("Times", 14, 'bold'))
        self.label4.place(x=80, y=205)

        self.pub = Entry(self.frame, font="Arial 12")
        self.pub.place(x=265, y=207)

        # creating Book price label and entry field
        self.label5 = Label(self.frame, text="PRICE")
        self.label5.config(font=("Times", 14, 'bold'))
        self.label5.place(x=80, y=245)

        self.prc = Entry(self.frame, font="Arial 12")
        self.prc.place(x=265, y=247)

        # creating Book category label and entry field
        self.label6 = Label(self.frame, text="BOOK CATEGORY")
        self.label6.config(font=("Times", 14, 'bold'))
        self.label6.place(x=75, y=285)

        self.cate = ['None', 'First Sem', 'Second Sem', 'Third Sem', 'Fourth Sem', 'Fifth Sem', 'Sixth Sem',
                     'Seventh Sem', 'Eighth Sem', 'Management', 'Technology', 'News paper', 'Magazines']
        self.cat = tk.StringVar(self.frame)
        self.droplist = tk.OptionMenu(self.frame, self.cat, *self.cate)
        self.droplist.config(width=24)
        self.cat.set(self.cate[0])
        self.droplist.place(x=262, y=287)

        self.label7 = Label(self.frame, text="All fields are mandatory...!", fg='red')
        self.label7.config(font=("Poppins", 10, 'underline bold'))
        self.label7.place(x=265, y=368)

        if self.data == '':
            self.btn = Button(self.frame, text='SUBMIT', width=15, bg='light grey', fg='black',
                              font=("Times", 13, "bold"), command=self.AddBook)
            self.btn.place(x=265, y=335)
        # else:
        #     up = dict(self.data).get('values')
        #     # set the values in input boxes
        #     self.bid.insert(0, up[0])
        #     self.bkt.insert(0, up[1])
        #     self.aut.insert(0, up[2])
        #     self.pub.insert(0, up[3])
        #     self.prc.insert(0, up[4])
        #     # self.cat.insert(0, up[5])
        #
        #     self.btn = Button(self.frame, text='UPDATE', width=15, bg='light grey', fg='black',
        #                       font=("Times", 13, "bold"), command=self.Update)
        #     self.btn.place(x=255, y=320)

        self.win.mainloop()

    def AddBook(self):
        data = (
            self.bid.get(),
            self.bkt.get(),
            self.aut.get(),
            self.pub.get(),
            self.prc.get(),
            self.cat.get(),
        )

        # it shows red color message if student id and name is not entered..
        if self.bid.get() == '':
            self.label1.config(fg='red')
            self.label1.config(text="Please enter Book Id", font=('Poppins', 11, 'bold'))

        elif self.bkt.get() == '':
            self.label2.config(fg='red')
            self.label2.config(text="Please enter Book title", font=('Poppins', 11, 'bold'))
            # code to clear the data from input box after submission
            self.bid.delete(0, 'end')
            self.bkt.delete(0, 'end')
            self.aut.delete(0, 'end')
            self.pub.delete(0, 'end')
            self.prc.delete(0, 'end')
            # self.cat.delete(0, 'end')

            # it shows error message if student id is same..and database is locked
        else:
            res = Database.database.AddBook(data)
            if res:
                k.showinfo("Alert..!", "Please enter valid details...!")

            else:
                k.showinfo("Welcome", "Book details added successfully...!")
                self.win.destroy()

    # def Update(self):
    #     data = (
    #         self.bid.get(),
    #         self.bkt.get(),
    #         self.aut.get(),
    #         self.pub.get(),
    #         self.prc.get(),
    #         self.cat.get(),
    #         dict(self.data).get('text')
    #     )
    #     res = Database.database.Update(data)
    #     if res:
    #         k.showinfo("Message", "Books details updated successfully")
    #         self.win.destroy()
    #         x = Student.Delete.DeleteWindow()
    #         x.add_frame()
