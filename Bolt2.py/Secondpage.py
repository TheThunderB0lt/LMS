# This is main page of Library Management System..

from tkinter import *
import Thirdpage
from PIL import ImageTk, Image
import tkinter.messagebox as nk


class MainWindow:

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
        self.win.title("| USER LOGIN | LIBRARY MANAGEMENT SYSTEM |")

    def add_frame(self):
        self.frame = Frame(self.win, height=540, width=960)
        self.frame.place(x=0, y=0)

        # x, y = 70, 20

        self.image = ImageTk.PhotoImage(Image.open("C:\\Users\\Nikith\\PycharmProjects\\Bolt2.py\\images\\man.png"))
        self.label = Label(self.frame, image=self.image)
        self.label.place(x=400, y=75)

        # creating login form for only admin can access
        self.label = Label(self.frame, text="USER LOGIN")
        self.label.config(font=("Courier", 20, 'underline bold'))
        self.label.place(x=380, y=220)

        # creating username label and entry field
        self.label1 = Label(self.frame, text="USERNAME")
        self.label1.config(font=("Times", 16, 'bold'))
        self.label1.place(x=240, y=290)

        self.user = Entry(self.frame, font="Times 12")
        self.user.place(x=385, y=292)

        # creating password label and entry field
        self.label2 = Label(self.frame, text="PASSWORD")
        self.label2.config(font=("Times", 16, 'bold'))
        self.label2.place(x=240, y=340)

        self.pswd = Entry(self.frame, font="Times 12", show="*")
        self.pswd.place(x=385, y=342)

        self.checkbox = Checkbutton(self.frame, text="Keep me logged in").place(x=380, y=375)

        self.btn = Button(self.frame, text='LOGIN', width=15, bg='light grey', fg='black', font=("Times", 13, "bold"),
                          command=self.login)
        self.btn.place(x=380, y=410)

    def login(self):
        data = (
            self.user.get(),
            self.pswd.get()
        )

        # if else condition for user authenticate..!
        if self.user.get() == "Admin" and self.pswd.get() == "160698":
            nk.showinfo("Login info", "Welcome To \n Library Management System...!")
            self.win.destroy()
            t = Thirdpage.ThirdWindow()
            t.add_menu()
            t.add_frame()
        else:
            nk.showinfo("Login error", "Invalid Username & Password")

        self.win.mainloop()
