from tkinter import *
from PIL import ImageTk
import time
import ttkthemes
from tkinter import ttk


# functionality
def clock():
    date = time.strftime("%B %d, %Y")
    current_time = time.strftime("%H:%M:%S")
    datetimeLabel.config(text=f"Date: {date}\nTime: {current_time}")
    datetimeLabel.after(1000,clock)


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

datetimeLabel = Label(root, text="Hello", font=("verdana", 18, "bold"))
datetimeLabel.place(x=0, y=0)
clock()
s = "Student Management System"
sliderLabel = Label(root, text=s, font=("verdana", 28, "italic bold"))
sliderLabel.place(x=420, y=0)
slider()

connectButton = ttk.Button(root, text="Connect Database")
connectButton.place(x=1135, y=0)

leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=200, height=600)

logoImage = PhotoImage(file="Resources/db.png")
logoImageLabel = Label(leftFrame, image=logoImage)
logoImageLabel.grid(row=0, column=0, padx=65, pady=10)

addStudentButton = ttk.Button(leftFrame, text="    Add Student", width=12)
addStudentButton.grid(row=1, column=0, pady=20)

searchStudentButton = ttk.Button(leftFrame, text="   Search Student", width=12)
searchStudentButton.grid(row=2, column=0, pady=20)

deleteStudentButton = ttk.Button(leftFrame, text="   Delete Student", width=12)
deleteStudentButton.grid(row=3, column=0, pady=20)

updateStudentButton = ttk.Button(leftFrame, text="   Update Student", width=12)
updateStudentButton.grid(row=4, column=0, pady=20)

showStudentButton = ttk.Button(leftFrame, text="   Show Student", width=12)
showStudentButton.grid(row=5, column=0, pady=20)

exportStudentButton = ttk.Button(leftFrame, text="   Export Student", width=12)
exportStudentButton.grid(row=6, column=0, pady=20)

exitButton = ttk.Button(leftFrame, text="          Exit", width=12)
exitButton.grid(row=7, column=0, pady=20)



root.mainloop()