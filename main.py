#Main fine, run from here.
import Debug
debug = Debug.Debug()
import LoginPage


import tkinter as tk
window = tk.Tk()
window.title("Hello World!")
window.grid()
width = 500
height = 300
window.geometry(f"{width}x{height}")

window.grid_rowconfigure(0, weight=1)  # Top row
window.grid_rowconfigure(1, weight=1)  # Middle row
window.grid_rowconfigure(2, weight=1)  # Bottom row
window.grid_columnconfigure(0, weight=1)  # Left column
window.grid_columnconfigure(1, weight=1)  # Center column
window.grid_columnconfigure(2, weight=1)  # Right column

def handle_button_press():
    debug.log("Hello world")



button = tk.Button(text= "My first app",command=handle_button_press).grid(column=1, row=1)



window.mainloop()