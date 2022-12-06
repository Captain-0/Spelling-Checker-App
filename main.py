import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="gray")


def check_spelling():
    word = enter_text.get()
    a = TextBlob(word)
    right = str(a.correct())

    cs = Label(root, text="Correct spelling is : ", font=("poppins", 20), bg="gray", fg="#364971")
    cs.place(x=100, y=250)
    spell.config(text=right)


heading = Label(root, text="SPELLING CHECKER", font=("Trebuchet MS", 30, 'bold'), bg="gray", fg="#364971")
heading.pack(pady=(50, 0))

enter_text = Entry(root, justify="center", width=30, font=("poppins", 25), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

button = Button(root, text="CHECK", font=("arial", 20, "bold"), fg="white", bg="red", command=check_spelling)
button.pack()

spell = Label(root, font=("poppins", 20), bg="gray", fg="yellow")
spell.place(x=350, y=250)

root.mainloop()
