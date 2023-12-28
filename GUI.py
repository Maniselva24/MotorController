import tkinter as tk
from tkinter import ttk
from TCP_Client import tcp_com

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Button Demo')
input_var = "hello"
L1 = ttk.Label(root, text="Data to Send")
L1.pack(
    ipadx=1,
    ipady=1,
    expand=True
)
E1 = tk.Entry(root, textvariable=input_var, font=('calibre', 10, 'normal'))
E1.pack(
    ipadx=1,
    ipady=1,
    expand=True
)


def on_click():
    tcp_com(E1.get())
    # print(E1.get())


# exit button
exit_button = ttk.Button(
    root,
    text='Start',
    command=on_click
)

exit_button.pack(
    ipadx=2,
    ipady=2,
    expand=True
)

root.mainloop()
