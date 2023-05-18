import tkinter as tk
from tkinter import *

class mygui:

    def __init__(self):
        self.root = tk.Tk()

        # Background Image
        bg = PhotoImage(file="rsz_2161439.png")
        label1 = Label(self.root, image=bg)
        label1.place(x=0, y=0)

        # Window Properties
        self.root.geometry("500x500")
        self.root.title("Connect Four")

        # Labels & Buttons
        self.label = tk.Label(self.root, text="Choose Difficulty", font=('Arial', 18))
        self.label.pack(padx=30, pady=30)

        self.button = tk.Button(self.root, text="Easy", font=('Arial', 15), command=self.select_diff())
        self.button.pack(padx=10, pady=20)

        self.button2 = tk.Button(self.root, text="Medium", font=('Arial', 15), command=self.select_diff2())
        self.button2.pack(padx=20, pady=20)

        self.button3 = tk.Button(self.root, text="Hard", font=('Arial', 15), command=self.select_diff3())
        self.button3.pack(padx=30, pady=20)

        self.root.mainloop()

    # Choosing Difficulty Which Changes The Depth Of The Search Algorithm
    def select_diff(self):
        return 4

    def select_diff2(self):
        return 5

    def select_diff3(self):
        return 6

mygui()
