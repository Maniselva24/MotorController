# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import tkinter

window = tkinter.Tk()
window.title("MotorX")
window.minsize(width=500, height=300)

# label
label_title = tkinter.Label(text="Motor Controller")
label_title.pack()

# should be end of the program
window.mainloop()
