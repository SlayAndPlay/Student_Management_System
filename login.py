from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


def login():
    if userEntry.get() == "" or passEntry.get() == "":
        messagebox.showerror("Error", "Fields cannot be empty!")
    elif userEntry.get() == "Christian" and passEntry.get() == "1234":
        messagebox.showinfo("Correct", "User Validated!")
        window.destroy()
        import sms

    else:
        messagebox.showerror("Error", "Please enter correct credentials!")


window = Tk()
window.geometry('1280x720+250+200')
window.resizable(False, False)
window.title("Login")


bgImage = ImageTk.PhotoImage(file="Resources/bg.jpg")
labelBg = Label(window, image=bgImage)
labelBg.place(x=0, y=0)


loginFrame = Frame(window)
loginFrame.place(x=470, y=220)
loginImage = PhotoImage(file="Resources/login.png")
loginImageLabel = Label(loginFrame, image=loginImage)
loginImageLabel.grid(row=0, column=0,columnspan=2, pady=10)

usernameImage = PhotoImage(file="Resources/id.png")
usernameLabel = Label(loginFrame,text="Username:", image=usernameImage, compound=LEFT,
                      font=("verdana", 16), padx=5)
usernameLabel.grid(row=1, column=0, pady=5)
passImage = PhotoImage(file="Resources/pass.png")
passLabel = Label(loginFrame,text="Password: ", image=passImage, compound=LEFT,
                  font=("verdana", 16), padx=5)
passLabel.grid(row=2, column=0, pady=5)

userEntry = Entry(loginFrame, bd=3)
userEntry.grid(row=1, column=1, padx=10)

passEntry = Entry(loginFrame, bd=3)
passEntry.grid(row=2, column=1, padx=10)

loginButton = Button(loginFrame, text="Login", font=("verdana", 10, "bold"), width=5,
                     cursor="hand",command=login)
loginButton.grid(row=3, column=0, columnspan=2)


window.mainloop()
