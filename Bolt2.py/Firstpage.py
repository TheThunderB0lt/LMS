# Main page of Library Management System..

from tkinter import *
import Secondpage
from PIL import ImageTk, Image


class Welcome:
    # creating a constructor
    def __init__(self):
        # creating tkinter window
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
        self.win.title("WELCOME | LIBRARY MANAGEMENT SYSTEM |")

    def add_frame(self):

        self.frame = Frame(self.win, height=540, width=960)
        self.frame.place(x=0, y=0)

        # x, y = 70, 20

        self.image = ImageTk.PhotoImage(Image.open("C:\\Users\\Nikith\\PycharmProjects\\Bolt2.py\\images\\lms.png"))
        self.label = Label(self.frame, image=self.image)
        self.label.pack()

        self.but = Button(self.frame, text='GO TO LOGIN >>', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.SecondPage)
        self.but.place(x=45, y=480)
        self.win.mainloop()

        # opening next window

    def SecondPage(self):
        # destroy current window
        self.win.destroy()
        # opens new window
        Main = Secondpage.MainWindow()
        Main.add_frame()


if __name__ == "__main__":
    x = Welcome()
    x.add_frame()
