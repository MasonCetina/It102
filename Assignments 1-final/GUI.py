"""
We are building a simple gui interface
"""

import tkinter as tk


# create main application windows
root = tk.Tk()
root.title("Simple Tkinter GUI")
root.geometry("400x300")

def on_click():
    label.config(text="Button Clicked!", fg="red")

#Create a label
label = tk.Label(root, text = "Click the button below!", font=("Arial", 14))
label.pack(pady=20)

#Create a button
button = tk.Button(root, text="click me", command=on_click)
button.pack()

#Run the application
root.mainloop()
