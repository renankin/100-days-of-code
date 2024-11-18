from tkinter import Tk, Label, Entry, Button


def miles_to_km():
    distance_miles = float(miles_entry.get())
    distance_km = round(1.609 * distance_miles, 1)
    result_label.config(text=str(distance_km))


# Window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Fixed labels
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Entry
miles_entry = Entry(width=5)
miles_entry.grid(column=1, row=0)

# Result label
result_label = Label(text="0")
result_label.grid(column=1, row=1)

# Calculate Button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=3)

window.mainloop()
