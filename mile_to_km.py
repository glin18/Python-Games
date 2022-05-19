from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def calculate():
    mile = entry.get()
    km = float(mile) * 1.609
    km_display.config(text=km)
    km_display.grid(column=1, row=1)


km_display = Label(text="")

entry = Entry(width=10)
entry.grid(column=1, row=0)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

window.mainloop()