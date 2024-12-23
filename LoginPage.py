# Login Page
import tkinter as tk
import Debug as debug

frm= tk.Tk()
frm.title("Login Page")
frm.grid()
width = 500
height = 300
# setting the heigt and width of the window.
frm.geometry(f"{width}x{height}")
# grid configuration to fit within the window equally no matter the size.
frm.grid_rowconfigure(0, weight=1)  # Top row
frm.grid_rowconfigure(1, weight=1)  # Middle row
frm.grid_rowconfigure(2, weight=1)  # Bottom row
frm.grid_columnconfigure(0, weight=1)  # Left column
frm.grid_columnconfigure(1, weight=1)  # Center column
frm.grid_columnconfigure(2, weight=1)  # Right column
def Login():
    userID = username
    password = password_entry
    debug.log("Loging In", "Working")
    if userID == "Admin" and password == "123":
        debug.log("Accepted")
    else:
        debug.log("Denyed", "ERROR")

username = tk.Entry(frm).grid(column=1,row=0)
password_entry = tk.Entry(frm, show="*").grid(column=1, row=1)
button = tk.Button(frm, text="Login", command=Login()).grid(column=1, row=2)
frm.mainloop()
