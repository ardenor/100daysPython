import tkinter

window = tkinter.Tk()

window.title("Title")
window.minsize(500, 300)

myLabel = tkinter.Label(text="Testing label", font=("Arial", 24, "bold"))
myLabel.pack(side="left")

myButton = tkinter.Button(text="Click me")
myButton.pack()












window.mainloop()