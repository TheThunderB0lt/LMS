# This page contains faculty details those who lending books form library

from tkinter import *
import tkinter.messagebox as n
import tkinter as tk
import Database.database


class FacultyWindow:

    def __init__(self):
        self.win = tk.Tk()
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
        self.win.title("| FACULTY REGISTRATION | LIBRARY MANAGEMENT SYSTEM |")

    def add_frame(self):
        self.frame = Frame(self.win, height=440, width=800)
        self.frame.place(x=0, y=0)

        # x, y = 70, 20

        # self.image = ImageTk.PhotoImage(Image.open("C:\\Users\\Nikith\\PycharmProjects\\Bolt2.py\\images\\man.png"))
        # self.label = Label(self.frame, image=self.image)
        # self.label.place(x=300, y=150)

        self.label = Label(self.frame, text="NEW FACULTY REGISTRATION", fg='black')
        self.label.config(font=("helvetica", 19, 'underline bold'))
        self.label.place(x=220, y=15)

        # creating student name label and entry field
        self.label1 = Label(self.frame, text="FACULTY ID")
        self.label1.config(font=("Times", 14, 'bold'))
        self.label1.place(x=80, y=80)

        self.id = Entry(self.frame, font="Arial 12")
        self.id.place(x=255, y=82)

        # creating student _id label and entry field
        self.label2 = Label(self.frame, text="FACULTY NAME")
        self.label2.config(font=("Times", 14, 'bold'))
        self.label2.place(x=80, y=120)

        self.name = Entry(self.frame, font="Arial 12")
        self.name.place(x=255, y=122)

        # creating student sem label and entry field
        self.label3 = Label(self.frame, text="GENDER")
        self.label3.config(font=("Times", 14, 'bold'))
        self.label3.place(x=80, y=160)

        self.gender = ['None', 'Male', 'Female']
        self.gen = tk.StringVar(self.frame)
        self.droplist = tk.OptionMenu(self.frame, self.gen, *self.gender)
        self.droplist.config(width=17)
        self.gen.set(self.gender[0])
        self.droplist.place(x=255, y=162)

        # self.gen = StringVar()
        # self.r1 = Radiobutton(self.frame, text='Male', variable=self.gen, value="Male").place(x=200, y=162)
        # self.r2 = Radiobutton(self.frame, text='Female', variable=self.gen, value="Female").place(x=255, y=162)
        # self.r3 = Radiobutton(self.frame, text='Other', variable=self.gen, value="Other").place(x=325, y=162)

        # self.gen = Entry(self.frame, font="Arial 12")
        # self.gen.place(x=205, y=162)

        # creating student dept label and entry field
        # self.label4 = Label(self.frame, text="SEMESTER")
        # self.label4.config(font=("Times", 14, 'bold'))
        # self.label4.place(x=80, y=200)
        #
        # self.semester = ['None', 'First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth']
        # self.sem = tk.StringVar(self.frame)
        # self.droplist = tk.OptionMenu(self.frame, self.sem, *self.semester)
        # self.droplist.config(width=17)
        # self.sem.set(self.semester[0])
        # self.droplist.place(x=255, y=202)

        # self.sem = Entry(self.frame, font="Arial 12")
        # self.sem.place(x=205, y=202)

        # creating student gender label and entry field
        self.label4 = Label(self.frame, text="DEPARTMENT")
        self.label4.config(font=("Times", 14, 'bold'))
        self.label4.place(x=80, y=200)

        self.list = ["NONE",
                     "CSE",
                     "ISE",
                     "ME",
                     "CIV",
                     "EEE",
                     "ECE"]
        self.dept = tk.StringVar(self.frame)
        self.drop = tk.OptionMenu(self.frame, self.dept, *self.list)
        self.drop.config(width=17)
        self.dept.set(self.list[0])
        self.drop.place(x=255, y=202)

        # self.dept = Entry(self.frame, font="Arial 12")
        # self.dept.place(x=205, y=242)

        # creating student phone no label and entry field
        self.label5 = Label(self.frame, text="CONTACT NO.")
        self.label5.config(font=("Times", 14, 'bold'))
        self.label5.place(x=80, y=240)

        self.con = Entry(self.frame, font="Arial 12")
        self.con.place(x=255, y=242)

        self.label6 = Label(self.frame, text="All fields are mandatory...!", fg='red')
        self.label6.config(font=("Poppins", 10, 'underline bold'))
        self.label6.place(x=250, y=325)

        self.btn = Button(self.frame, text='SUBMIT', width=15, bg='light grey', fg='black', font=("Times", 13, "bold"),
                          command=self.FacultyReg)
        self.btn.place(x=255, y=280)

        self.win.mainloop()

    def FacultyReg(self):
        data = (
            self.id.get(),
            self.name.get(),
            self.gen.get(),
            self.dept.get(),
            self.con.get()
        )

        # it shows red color message if student id and name is not entered..
        if self.id.get() == '':
            self.label1.config(fg='red')
            self.label1.config(text="Please enter Faculty_ID", font=('Poppins', 11, 'bold'))

        elif self.name.get() == '':
            self.label2.config(fg='red')
            self.label2.config(text="Please enter Faculty_Name", font=('Poppins', 10, 'bold'))

            # it shows error message if student id is same..and database is locked
        else:
            res = Database.database.FacultyReg(data)
            if res:
                n.showinfo("Alert..!", "Please enter valid details...!")

            else:
                n.showinfo("Welcome", "Faculty details added successfully...!")
                self.win.destroy()
