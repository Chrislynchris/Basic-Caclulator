import tkinter as tk
from tkinter import messagebox
import math

# Function to handle button clicks
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)  # Clear the entry field
    entry.insert(tk.END, current + str(value))  # Add the clicked value

# Function to clear the display
def button_clear():
    entry.delete(0, tk.END)

# Function to delete the last character
def button_backspace():
    current = entry.get()
    entry.delete(len(current)-1, tk.END)

# Function to calculate the result
def button_equal():
    try:
        # Replace square root symbol with Python's recognized sqrt function
        expression = entry.get().replace('√', 'math.sqrt')
        result = eval(expression)  # Evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")
        entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")
        entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title(" Calculator By Christabel")
root.geometry("400x550")  # Set a fixed window size
root.config(bg="#2C3E50")  # Dark theme background

# Create the entry widget (where the user will see input and results)
entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=2, relief="solid", justify="right", bg="#ECF0F1", fg="#2C3E50")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Define button layout (including the square root and exponentiation)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('√', 5, 0), ('^', 5, 1), ('C', 5, 2), ('<', 5, 3)
]

# Function to create a button with styling
def create_button(root, text, row, col, width=5, height=2, font=('Arial', 20), bg="#34495E", fg="#ECF0F1", command=None):
    button = tk.Button(root, text=text, width=width, height=height, font=font, bg=bg, fg=fg, command=command)
    button.grid(row=row, column=col, padx=5, pady=5)
    return button

# Create buttons and add them to the grid
for (text, row, col) in buttons:
    if text == '=':
        create_button(root, text, row, col, bg="#16A085", command=button_equal)
    elif text == 'C':
        create_button(root, text, row, col, bg="#E74C3C", command=button_clear)
    elif text == '<':
        create_button(root, text, row, col, bg="#F39C12", command=button_backspace)
    else:
        create_button(root, text, row, col, bg="#34495E", command=lambda value=text: button_click(value))

# Run the main loop
root.mainloop()
