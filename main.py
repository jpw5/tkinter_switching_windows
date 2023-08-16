import customtkinter as ctk
import tkinter
from tkinter import ttk, messagebox

def switch():
    button.pack_forget()
    back_button.pack()

def back():
    back_button.pack_forget()
    button.pack()

root = ctk.CTk()
root.title('Test')
root.geometry('300x300')

button = ctk.CTkButton(root, text='Switch Window', command=switch)
button.pack()

back_button = ctk.CTkButton(root, text='Main Menu', command=back)





root.mainloop()
