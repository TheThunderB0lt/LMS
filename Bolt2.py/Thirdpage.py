# this is third page which contains all library information..

from tkinter import *
from PIL import ImageTk, Image
import Student.StudentReg
import Student.FacultyReg
import Student.AddBook
import Student.BookLending
import Student.FacultyBook
import Student.ViewStudents
import Student.FacultyDetails
import Student.ViewBooks
import Student.ViewLending
import Student.ViewFaculty
import Student.Delete
import Student.DeleteFaculty
import Student.DeleteStudents
import Student.Return
import Student.FacultyRet
import webbrowser


def StudentReg():
    x = Student.StudentReg.StudentWindow()
    x.add_frame()


def FacultyReg():
    x = Student.FacultyReg.FacultyWindow()
    x.add_frame()


def AddBook():
    x = Student.AddBook.BooksWindow()
    x.add_frame()


def BookLending():
    x = Student.BookLending.BookLendingWindow()
    x.add_frame()


def BookLend():
    x = Student.FacultyBook.FacultyBookWindow()
    x.add_frame()


def FacultyBook():
    x = Student.ViewFaculty.FacultyBookLendWindow()
    x.add_frame()


def ViewStudents():
    x = Student.ViewStudents.ViewWindow()
    x.add_frame()


def FacultyDetails():
    x = Student.FacultyDetails.ViewFacultyDetailsWindow()
    x.add_frame()


def ViewBooks():
    x = Student.ViewBooks.ViewBookWindow()
    x.add_frame()


def ViewLending():
    x = Student.ViewLending.BookLendingWindow()
    x.add_frame()


def Delete():
    x = Student.Delete.DeleteWindow()
    x.add_frame()


def DeleteFaculty():
    x = Student.DeleteFaculty.FacultyDelWindow()
    x.add_frame()


def DeleteStudents():
    x = Student.DeleteStudents.DeleteStudWindow()
    x.add_frame()


def Return():
    x = Student.Return.ReturnWindow()
    x.add_frame()


def FacultyRet():
    x = Student.FacultyRet.FacultyReturnWindow()
    x.add_frame()


url = 'http://localhost:63342/Bolt2.py/images/ourteam.html?_ijt=uphcd7jfa694pbj9rhqgn15sag'


def OpenUrl():
    webbrowser.open(url)


def back():
    exit()


class ThirdWindow:

    def __init__(self):
        self.win = Tk()

        # window background color using canvas
        self.canvas = Canvas(self.win, width=960, height=540, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 960 / 2)
        y = int(height / 2 - 540 / 2)
        str1 = "960x540+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        # disable resize window
        self.win.resizable(False, False)

        # changing title of the window
        self.win.title("| LIBRARY MENU | LIBRARY MANAGEMENT SYSTEM |")

    def add_menu(self):
        # crating main menu
        self.mainmenu = Menu(self.win)
        self.win.config(menu=self.mainmenu)

        # creating first menu list tearoff=0
        self.first = Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="STUDENT", menu=self.first)
        self.first.add_command(label="ADDING STUDENT DETAILS", command=StudentReg)

        # creating first menu list tearoff=0
        self.sec = Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="FACULTY", menu=self.sec)
        self.sec.add_command(label="ADDING FACULTY DETAILS", command=FacultyReg)

        # creating second menu list
        self.second = Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="BOOKS ", menu=self.second)
        self.second.add_command(label="ADDING NEW BOOKS", command=AddBook)
        self.second.add_separator()
        self.second.add_command(label="STUDENT BOOK_LENDING", command=BookLending)
        self.second.add_separator()
        self.second.add_command(label="FACULTY BOOK_LENDING", command=BookLend)

        # creating third menu list
        self.third = Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="VIEW BY", menu=self.third)
        self.third.add_command(label="VIEW BY STUDENT DETAILS", command=ViewStudents)
        self.third.add_separator()
        self.third.add_command(label="VIEW BY FACULTY DETAILS", command=FacultyDetails)
        self.third.add_separator()
        self.third.add_command(label="VIEW BY BOOK DETAILS", command=ViewBooks)
        self.third.add_separator()
        self.third.add_command(label="VIEW BY STUDENT BOOK_LENDING", command=ViewLending)
        self.third.add_separator()
        self.third.add_command(label="VIEW BY FACULTY BOOK_LENDING", command=FacultyBook)

        # creating fourth menu list
        self.four = Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="DELETE", menu=self.four)
        self.four.add_command(label="DELETING BOOK DETAILS", command=Delete)
        self.four.add_separator()
        self.four.add_command(label="DELETING STUDENT DETAILS", command=DeleteStudents)
        self.four.add_separator()
        self.four.add_command(label="DELETING FACULTY DETAILS", command=DeleteFaculty)

        # creating fifth menu list
        self.five = Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="RETURN", menu=self.five)
        self.five.add_command(label="RETURNING BOOK_LENDING BY  STUDENT", command=Return)
        self.five.add_command(label="RETURNING BOOK_LENDING BY  FACULTY", command=FacultyRet)

        # creating sixth menu list
        self.six = Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="ABOUT", menu=self.six)
        self.six.add_command(label="!..ADMIN ..!", command=OpenUrl)

        # creating seventh menu list
        self.seven = Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="CLOSE", menu=self.seven)
        self.seven.add_command(label="((''..''))...QUIT...((''..''))", command=back)

    def add_frame(self):
        self.image = ImageTk.PhotoImage(Image.open("C:\\Users\\Nikith\\PycharmProjects\\Bolt2.py\\images\\b.jpg"))
        self.label = Label(self.win, image=self.image)
        self.label.place(x=0, y=0)

        self.win.mainloop()


if __name__ == "__main__":
    x = ThirdWindow()
    x.add_menu()
    x.add_frame()
