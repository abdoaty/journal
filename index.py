import tkinter as tk
from tkinter import ttk
from datetime import datetime
import os

window = tk.Tk()

# Function to save the journal entry
def save():
    journal_date = datetime.today().strftime('%Y-%m-%d')
    file_name = f"journal_{journal_date}.txt"
    entry_text = text.get("1.0", tk.END)

    try:
        with open(file_name, "a") as file:
            file.write(entry_text)
        status_label.config(text=f"Entry saved to {file_name}")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

# Function to close the application
def close_app():
    window.destroy()

# Widgets
journal_date = datetime.today().strftime('%Y-%m-%d')
label = tk.Label(master=window, text='Journal Entry for: ' + journal_date)
text = tk.Text(master=window)
button_save = tk.Button(master=window, text='Save', command=save)
button_close = tk.Button(master=window, text='Close', command=close_app)
status_label = tk.Label(master=window, text='')

# Packing widgets
label.pack()
text.pack()
button_save.pack(side='left')
button_close.pack(side='right')
status_label.pack()

# Run the Tkinter main loop
window.mainloop()
