#Main fine, run from here.
import subprocess
import Debug as db
import tkinter as tk



#creating the main window.
window = tk.Tk()
#giving it a custom title.
window.title("Hello World!")
window.grid()
width = 500
height = 300
#setting the heigt and width of the window.
window.geometry(f"{width}x{height}")
#grid configuration to fit within the window equally no matter the size.
window.grid_rowconfigure(0, weight=1)  # Top row
window.grid_rowconfigure(1, weight=1)  # Middle row
window.grid_rowconfigure(2, weight=1)  # Bottom row
window.grid_columnconfigure(0, weight=1)  # Left column
window.grid_columnconfigure(1, weight=1)  # Center column
window.grid_columnconfigure(2, weight=1)  # Right column
#What happens on the press of the button.
def handle_button_press():
    window.destroy()
    subprocess.run(["python", "LoginPage.py"])

#declaring the button.
button = tk.Button(text= "My first app",command=handle_button_press).grid(column=1, row=1)

window.mainloop()
