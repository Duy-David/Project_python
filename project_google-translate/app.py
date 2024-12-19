from tkinter import *
from googletrans import Translator
from PIL import Image, ImageTk


# tạo màn hình window
root = Tk()
root.title("Google Phương Duy")
root.geometry("500x630")
root.iconbitmap("logo.ico")
backgroud = Image.open("background.png")
render = ImageTk.PhotoImage(backgroud)
img = Label(root, image=render)
img.place(x=0, y=0)

name = Label(root, text="Translator", fg="#FFFFFF", bd=0, bg="#03152D")
name.config(font=("Transformers Movie", 30))
name.pack(pady=10)


box = Text(root, width=28, height=8, font=("ROBOTO", 16))
box.pack(pady=20)

button_frame = Frame(root).pack(side=BOTTOM)


def clear():
    box.delete(1.0, END)
    box1.delete(1.0, END)


def translate():
    input = box.get(1.0, END)
    trans = Translator()
    # Dịch văn bản
    translated = trans.translate(text=input, dest="en", src="vi")
    box1.insert(END, translated.text)


clear_button = Button(
    button_frame,
    text="Clear text",
    font=(("Arial"), 10, "bold"),
    bg="#303030",
    fg="#ffffff",
    command=clear,
)
clear_button.place(x=150, y=310)

trans_button = Button(
    button_frame,
    text="Translate text",
    font=(("Arial"), 10, "bold"),
    bg="#303030",
    fg="#ffffff",
    command=translate,
)
trans_button.place(x=290, y=310)

box1 = Text(root, width=28, height=8, font=("ROBOTO", 16))
box1.pack(pady=50)

root.mainloop()
