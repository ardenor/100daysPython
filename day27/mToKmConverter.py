from tkinter import *
window = Tk()

window.title("M to KM Converter")
window.config(padx=20, pady=20)
# window.minsize(500, 300)


input = Entry(width=10)
input.insert(END, string="0")
input.grid(column=2, row=0)

resultLabel = Label(text="0", font=("Arial", 24, "bold"))
resultLabel.grid(column=2, row=1)

milesLabel = Label(text="Miles")
milesLabel.grid(column=3, row=0)

kmLabel = Label(text="Km")
kmLabel.grid(column=3, row=1)

equalsLabel = Label(text="is equal to")
equalsLabel.grid(column=0, row=1)

def button_clicked():
    if input.get() == "Exit":
        exit(0)
    else:
        resultLabel["text"] = float(input.get()) * 1.609

myButton = Button(text="Calculate", command=button_clicked)
myButton.grid(column=2, row=2)





window.mainloop()