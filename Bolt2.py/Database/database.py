import sqlite3
import datetime


# Creating and inserting student details..!

def StudentReg(data):
    conn = sqlite3.connect("Library.db")
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS Student ("STUDENT_ID" INTEGER, "FULL_NAME" TEXT, "GENDER" TEXT, '
        '"SEM" TEXT, "DEPARTMENT" TEXT, "PHONE_NO" INTEGER, PRIMARY KEY("STUDENT_ID"))')
    cur.execute('INSERT INTO Student VALUES(?,?,?,?,?,?)', data)
    conn.commit()


def FacultyReg(data):
    conn = sqlite3.connect("Library.db")
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS Faculty ("FACULTY_ID" INTEGER, "FACULTY_NAME" TEXT, "GENDER" TEXT, "DEPARTMENT" '
        'TEXT, "CONTACT_NO" INTEGER, PRIMARY KEY("FACULTY_ID"))')
    cur.execute('INSERT INTO Faculty VALUES(?,?,?,?,?)', data)
    conn.commit()


# Creating and inserting book details..!


def AddBook(data):
    conn = sqlite3.connect("Library.db")
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS Books ("BOOK_ID" INTEGER, "BOOK_TITLE" TEXT, "AUTHOR_NAME" TEXT, '
        '"PUBLISHED_YEAR" INTEGER, "PRICE"	INTEGER, "BOOK_CATEGORY" TEXT, PRIMARY KEY("BOOK_ID"))')
    cur.execute('INSERT INTO Books VALUES(?,?,?,?,?,?)', data)
    conn.commit()

    # Creating and inserting book details..!


def BookLending(data, id):
    status = 0
    id_status = 0
    print(data, type(data[3]))
    conn = sqlite3.connect("Library.db")
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS BookLending ("BOOK_ID" references Books on DELETE CASCADE, "STUDENT_ID"'
        'references Student on DELETE CASCADE, "ISSUE_DATE" INTEGER, "RETURN_DATE" INTEGER, "FINE" INTEGER, '
        'PRIMARY KEY("BOOK_ID", "STUDENT_ID"))')
    cur.execute('SELECT COUNT(*) FROM BookLending B, Student S where B.STUDENT_ID = ? and S.STUDENT_ID = ?', id)
    id_count = cur.fetchone()
    print(type(id_count), id_count[0])
    if id_count[0] <= 2:
        id_status = 1
        cur.execute('INSERT INTO BookLending VALUES(?,?,?,?,0)', data)
    else:
        id_status = 0
    status = 1
    conn.commit()
    return int(status), int(id_status)


def FacultyBookLending(data, id):
    status = 0
    id_status = 0
    print(data, type(data[3]))
    conn = sqlite3.connect("Library.db")
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS FacultyBookLending ("BOOK_ID" references Books on DELETE CASCADE, "Faculty_ID"'
        'references Faculty on DELETE CASCADE, "ISSUE_DATE" INTEGER, "RETURN_DATE" INTEGER, "FINE" INTEGER, '
        'PRIMARY KEY("BOOK_ID", "FACULTY_ID"))')
    cur.execute('SELECT COUNT(*) FROM FacultyBookLending B, Faculty S where B.FACULTY_ID = ? and S.FACULTY_ID = ?', id)
    id_count = cur.fetchone()
    print(type(id_count), id_count[0])
    if id_count[0] <= 2:
        id_status = 1
        cur.execute('INSERT INTO FacultyBookLending VALUES(?,?,?,?,0)', data)
    else:
        id_status = 0
    status = 1
    conn.commit()
    return int(status), int(id_status)


def ViewStudents():
    conn = sqlite3.connect("Library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Student")
    return cur.fetchall()


def ViewBooks():
    conn = sqlite3.connect("Library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Books")
    return cur.fetchall()


def BookLend():
    conn = sqlite3.connect("Library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM BookLending")
    return cur.fetchall()


def Faculties():
    conn = sqlite3.connect("Library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Faculty")
    return cur.fetchall()


def FacultyBookLend():
    conn = sqlite3.connect("Library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM FacultyBookLending")
    return cur.fetchall()


def DeleteStudent(data):
    conn = sqlite3.connect("Library.db")
    cur = conn.cursor()
    cur.execute('DELETE FROM Student WHERE STUDENT_ID = ?', data)
    conn.commit()
    return True


def DeleteFaculty(data):
    conn = sqlite3.connect("Library.db")
    cur = conn.cursor()
    cur.execute('DELETE FROM Faculty WHERE FACULTY_ID = ?', data)
    conn.commit()
    return True


# def Update(data):
#     conn = sqlite3.connect("Library.db")
#     cur = conn.cursor()
#     cur.execute('UPDATE Books SET BOOK_ID = ?, BOOK_TITLE = ?, AUTHOR_NAME = ?, PUBLISHED_YEAR = ?, PRICE = ? WHERE '
#                 'BOOK_ID = ?', data)
#     conn.commit()
#     return True


def Delete(data):
    conn = sqlite3.connect("Library.db")
    cur = conn.cursor()
    cur.execute('DELETE FROM Books WHERE BOOK_ID = ?', data)
    conn.commit()
    return True


def Return(data):
    conn = sqlite3.connect("Library.db")
    cur = conn.cursor()
    print(data)
    date_format = "%m/%d/%Y"
    today = datetime.date.today()
    current_date = str(today.strftime("%m/%d/%Y"))
    print(type(current_date))
    cur.execute('select return_date from BookLending where book_id = ? and student_id = ?', data)
    return_date = cur.fetchone()
    fine_days = (datetime.datetime.strptime(current_date, date_format) - datetime.datetime.strptime(return_date[0],
                                                                                                    date_format)).total_seconds() / 60 / 60 / 24
    fine_days = int(fine_days)
    cur.execute("delete from BookLending where book_id =? and student_id = ?", data)
    print(fine_days)
    fine_days = fine_days * 2
    if fine_days <= 0:
        fine_days = 0
    conn.commit()
    return True, fine_days


def FacultyReturn(data):
    conn = sqlite3.connect("Library.db")
    cur = conn.cursor()
    print(data)
    date_format = "%m/%d/%Y"
    today = datetime.date.today()
    current_date = str(today.strftime("%m/%d/%Y"))
    print(type(current_date))
    cur.execute('select return_date from FacultyBookLending where book_id = ? and faculty_id = ?', data)
    return_date = cur.fetchone()
    fine_days = (datetime.datetime.strptime(current_date, date_format) - datetime.datetime.strptime(return_date[0],
                                                                                                    date_format)).total_seconds() / 60 / 60 / 24
    fine_days = int(fine_days)
    cur.execute("delete from FacultyBookLending where book_id =? and faculty_id = ?", data)
    print(fine_days)
    fine_days = fine_days * 0
    if fine_days <= 0:
        fine_days = 0
    conn.commit()
    return True, fine_days


def filter(search_text):
    conn = sqlite3.connect("Library.db")
    cur = conn.cursor()
    cur.execute('select * from Books where book_category = ?', search_text)
    data = cur.fetchall()
    conn.commit()
    return data
