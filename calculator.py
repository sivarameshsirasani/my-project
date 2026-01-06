import tkinter as tk

# 1. Function for button click
def button_click(number):
    current = entry_field.get()
    entry_field.delete(0, tk.END)
    entry_field.insert(0, current + str(number))

# 2. Function to clear the screen (C button)
def button_clear():
    entry_field.delete(0, tk.END)

# 3. Function to calculate the result (= button)
def button_equal():
    try:
        result = eval(entry_field.get()) # 'eval' automatically calculates the math
        entry_field.delete(0, tk.END)
        entry_field.insert(0, str(result))
    except:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, "Error")

# Window Setup
root = tk.Tk()
root.title("Simple Calculator")

# Display Screen (Entry box)
entry_field = tk.Entry(root, width=35, borderwidth=5)
entry_field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Create Buttons

# Row 1
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))

# Row 2
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))

# Row 3
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))

# Row 4 (0, Clear, Equal)
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = tk.Button(root, text="+", padx=39, pady=20, command=lambda: button_click("+"))
button_equal = tk.Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# Other Operators
button_subtract = tk.Button(root, text="-", padx=41, pady=20, command=lambda: button_click("-"))
button_multiply = tk.Button(root, text="*", padx=40, pady=20, command=lambda: button_click("*"))
button_divide = tk.Button(root, text="/", padx=41, pady=20, command=lambda: button_click("/"))

# Placing buttons on the screen (Grid System)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

# Start the application
root.mainloop()