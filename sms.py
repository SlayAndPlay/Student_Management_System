from tkinter import *
from PIL import ImageTk
import time
import ttkthemes
from tkinter import ttk, messagebox
import pymysql


# functionality
def connectDB():
    def connect():
        try:
            connection = pymysql.connect(host=hostEntry.get(), user=userEntry.get(),
                                         password=passEntry.get())
            myCursor = connection.cursor()
        except:
            messagebox.showerror("Error", "Invalid Details", parent=dbWin)
            return
        try:
            query = 'create database studentmanagementsystem'
            myCursor.execute(query)
            query = 'use studentmanagementsystem'
            myCursor.execute(query)
            query = 'create table student(id int not null primary key, name varchar(30), mobile varchar(10), email varchar(30),' \
                    'address varchar(100), gender varchar(20), dob varchar(20), date varchar(50),' \
                    'time varchar(50))'
            myCursor.execute(query)
        except:
            query="use studentmanagementsystem"
            myCursor.execute(query)
        messagebox.showinfo("Success", "Database Connection is successful", parent=dbWin)
        addStudentButton.config(state=NORMAL)
        searchStudentButton.config(state=NORMAL)
        updateStudentButton.config(state=NORMAL)
        showStudentButton.config(state=NORMAL)
        exportStudentButton.config(state=NORMAL)
        deleteStudentButton.config(state=NORMAL)
        dbWin.destroy()


    dbWin = Toplevel()
    dbWin.grab_set()
    dbWin.title("Connect to Database")
    dbWin.geometry("400x300+700+400")
    dbWin.resizable(False, False)

    hostnameLabel = Label(dbWin, text="Hostname:  ", font=("verdana", 20, "bold"))
    hostnameLabel.grid(row=0, column=0, padx=5, pady=15)

    hostEntry = Entry(dbWin, font=("verdana", 15, "bold"), bd=1)
    hostEntry.grid(row=0, column=1, padx=5, pady=15)

    usernameLabel = Label(dbWin, text="Username:  ", font=("verdana", 20, "bold"))
    usernameLabel.grid(row=1, column=0, padx=5, pady=15)

    userEntry = Entry(dbWin, font=("verdana", 15, "bold"), bd=1)
    userEntry.grid(row=1, column=1, padx=5, pady=15)

    passLabel = Label(dbWin, text="Password:  ", font=("verdana", 20, "bold"))
    passLabel.grid(row=2, column=0, padx=5, pady=15)

    passEntry = Entry(dbWin, font=("verdana", 15, "bold"), bd=1, show="*")
    passEntry.grid(row=2, column=1, padx=5, pady=15)

    connectDBButton = ttk.Button(dbWin, text="Connect", command=connect)
    connectDBButton.grid(row=3, column=0, columnspan=2)

    dbWin.mainloop()


def close():
    root.destroy()


def clock():
    date = time.strftime("%B %d, %Y")
    current_time = time.strftime("%H:%M:%S")
    datetimeLabel.config(text=f"Date: {date}\nTime: {current_time}")
    datetimeLabel.after(1000, clock)


count = 0
text = ''


def slider():
    global text, count
    if count == len(s):
        count = 0
        text = ''
    text = text + s[count]
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(100, slider)


# gui
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme("clearlooks")
root.geometry("1280x720+250+200")
root.title("SMS made with ❤️")
root.resizable(False, False)
smsBg = ImageTk.PhotoImage(file="Resources/smsbg.jpg")
labelSms = Label(root, image=smsBg)
labelSms.place(x=0, y=0)

datetimeLabel = Label(root, text="Hello", font=("verdana", 18, "bold"), bg="white", fg="black")
datetimeLabel.place(x=0, y=0)
clock()
s = "Student Management System"
sliderLabel = Label(root, text=s, font=("verdana", 28, "italic bold"), bg="white", fg="black")
sliderLabel.place(x=420, y=0)
slider()

connectButton = ttk.Button(root, text="Connect Database", command=connectDB)
connectButton.place(x=1135, y=0)

leftFrame = Frame(root, bg="white")
leftFrame.place(x=50, y=80, width=200, height=600)

logoImage = PhotoImage(file="Resources/db.png")
logoImageLabel = Label(leftFrame, image=logoImage, bg="white")
logoImageLabel.grid(row=0, column=0, padx=65, pady=10)

addStudentButton = ttk.Button(leftFrame, text="    Add Student", width=12, state=DISABLED)
addStudentButton.grid(row=1, column=0, pady=20)

searchStudentButton = ttk.Button(leftFrame, text="   Search Student", width=12, state=DISABLED)
searchStudentButton.grid(row=2, column=0, pady=20)

deleteStudentButton = ttk.Button(leftFrame, text="   Delete Student", width=12, state=DISABLED)
deleteStudentButton.grid(row=3, column=0, pady=20)

updateStudentButton = ttk.Button(leftFrame, text="   Update Student", width=12, state=DISABLED)
updateStudentButton.grid(row=4, column=0, pady=20)

showStudentButton = ttk.Button(leftFrame, text="   Show Student", width=12, state=DISABLED)
showStudentButton.grid(row=5, column=0, pady=20)

exportStudentButton = ttk.Button(leftFrame, text="   Export Student", width=12, state=DISABLED)
exportStudentButton.grid(row=6, column=0, pady=20)

exitButton = ttk.Button(leftFrame, text="            Exit", width=12, command=close)
exitButton.grid(row=7, column=0, pady=20)

rightFrame = Frame(root)
rightFrame.place(x=350, y=80, width=900, height=600)

scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

studentTable = ttk.Treeview(rightFrame, columns=("1", "2", "3", "4", "5", "6",
                                                 "7", "8", "9"), xscrollcommand=scrollBarX.set,
                            yscrollcommand=scrollBarY.set)

studentTable.heading("1", text="ID")
studentTable.heading("2", text="Name")
studentTable.heading("3", text="Phone")
studentTable.heading("4", text="Email")
studentTable.heading("5", text="Address")
studentTable.heading("6", text="Gender")
studentTable.heading("7", text="DOB")
studentTable.heading("8", text="Added Date")
studentTable.heading("9", text="Added Time")

studentTable.config(show="headings")

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)

studentTable.pack(fill=BOTH, expand=1)

root.mainloop()
