from tkinter import *
from tkinter import messagebox


def login():
    username = username_entry.get()
    password = password_entry.get()
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title='Login Success', message='You successfully loged in')
    else:
        messagebox.showerror(title='ERROR', message='Invalid Login')


window = Tk()
window.title('Login Form')
window.geometry('600x440')
window.config(bg='#333333')

frame = Frame(bg='#333333')  # we add this to place our widgets in the middle of the screen

# Creating widgets
login_label = Label(frame, text='Login', bg='#333333', fg='#FF3399', font=('Arial', 30))
username_label = Label(frame, text='Username', bg='#333333', fg='#FFFFFF', font=('Arial', 16))
username_entry = Entry(frame, font=('Arial', 16))
password_label = Label(frame, text='Password', bg='#333333', fg='#FFFFFF', font=('Arial', 16))
password_entry = Entry(frame, show='*', font=('Arial', 16))
login_button = Button(frame, text='Login', bg='#FF3399', fg='#FFFFFF', font=('Arial', 16), command=login)


# pady - more spacing

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()
