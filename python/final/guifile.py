import math
from tkinter import *
from tkinter import messagebox
def show_message():
 messagebox.showinfo("Math Calculator", "სფეროს მოცულობა: "+ str((4 / 3) * math.pi * int(message.get())))

root = Tk()
root.title("Math Calculator")
root.geometry("500x500")
label1 = Label(text="სფეროს მოცულობა", fg="#eee",
 bg="#333")
label1.pack()
message = StringVar()
message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")
message_button = Button(text="Result",
 command=show_message)
message_button.place(relx=.5, rely=.2, anchor="c")
root.mainloop()