import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="gray")

heading = Label(root, text="SPELLING CHECKER", font=("Trebuchet MS", 30, 'bold'), bg="gray", fg="#364971")
heading.pack(pady=(50, 0))

root.mainloop()
