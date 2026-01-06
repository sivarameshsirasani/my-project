import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("My Digital Clock")
root.resizable(False, False) # User cannot resize the window

# Function to update the time
def time():
    string = strftime('%H:%M:%S %p') # Format: Hours:Minutes:Seconds AM/PM
    label.config(text=string)
    label.after(1000, time) # Run this function again after 1000ms (1 second)

# Design (Font, Background color, Text color)
label = tk.Label(root, font=('calibri', 50, 'bold'),
                 background='black',
                 foreground='cyan') 

# Placing the label in the center
label.pack(anchor='center')

# Call the time function to start the clock
time() 

# Main loop to keep the window open
root.mainloop()