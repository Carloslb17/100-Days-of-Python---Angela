from tkinter import *


def formula_to_km():
    miles =miles_input.get()
    km = float(miles) * 1.6
    kilometer_result_label.config(text=f"{km}")
window = Tk()
#Windowe
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)


kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=formula_to_km)
calculate_button.grid(column=2, row=4)

window.mainloop()