import tkinter as tk
from tkinter import ttk
from TCP_Client import tcp_send, tcp_receive

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Button Demo')
input_var = "hello"
L1 = ttk.Label(root, text="")

E1 = tk.Entry(root, textvariable=input_var, font=('calibre', 10, 'normal'))


def send_click():
    tcp_send(E1.get())


def receive_click():
    L1.config(text=tcp_receive())

    # L1.config(text=tcp_send(E1.get()))
    # print(E1.get())


# exit button
send_btn = ttk.Button(
    root,
    text='Send',
    command=send_click
)
E1.pack(
    ipadx=1,
    ipady=1,
    expand=True
)

send_btn.pack(
    ipadx=2,
    ipady=2,
    expand=True
)
L1.pack(
    ipadx=1,
    ipady=1,
    expand=True
)
receive_btn = ttk.Button(
    root,
    text='Receive',
    command=receive_click
)

receive_btn.pack(
    ipadx=2,
    ipady=2,
    expand=True
)

root.mainloop()
