from tkinter import *


def button_clicked():
    my_label.config(text=input_window.get())


# Window
window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# New Button
new_button = Button(text="Don't click me")
new_button.grid(column=2, row=0)

# Entry
input_window = Entry(width=10)
input_window.grid(column=3, row=3)

window.mainloop()

