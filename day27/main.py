# import tkinter
from tkinter import *

window = Tk()

window.title("Title")
window.minsize(500, 300)
window.config(padx=20, pady=20)

myLabel = Label(text="Testing label", font=("Arial", 24, "bold"))
myLabel["text"] = "This is a test"
# myLabel.config(text="This is a test")
# myLabel.pack(side="left")
# myLabel.place(x=100, y=100)
myLabel.grid(column=0, row=0)
myLabel.config(padx=50, pady=50)

#Button
def button_clicked():
    if input.get() == "Exit":
        exit(0)
    else:
        myLabel["text"] = input.get()

myButton = Button(text="Click me", command=button_clicked)
# myButton.pack()
myButton.grid(column=1, row=1)

myButton2 = Button(text="Click me", command=button_clicked)
# myButton.pack()
myButton2.grid(column=2, row=0)




#Input
input = Entry(width=10)
input.insert(END, string="Starting text")
# input.pack()
input.grid(column=3, row=2)
print(input.get())

# #Textbox
# textbox = Text(height=5, width=30)
# #puts cursor in textbox
# textbox.focus()
# #add some text to begin with
# textbox.insert(END, "Example")
# #gets current value in textbox at line1, character 0
# print(textbox.get("1.0", END))
# textbox.pack()
#
# #Spinbox
# def spinbox_used():
#     #gets current value in spinbox
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# #Scale
# #called with current scale value
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# #checkbutton
# def checkbutton_used():
#     #prints 1 if on button check, otherwise 0
#     print(checked_state.get())
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# #radiobutton
# def radio_used():
#     print(radio_state.get())
# #variable to hold on to which radio button value is checked
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
# #Listbox
# def listbox_used(event):
#     #gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()


window.mainloop()