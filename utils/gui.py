from tkinter import *


def init_tkinter():
    tk = Tk()
    tk.title('AC')
    tk.wm_attributes("-topmost", 1)
    Width = 600
    Height = 600
    canvas = Canvas(tk, width=Width, height=Height, bg='white', highlightthickness=0)
    canvas.pack()
    canvas.create_line(Height - 150, Height - 150, Height - 150, Height, Height - 150, Height - 150, Height, Height - 150)
    tk.update()
    return tk, canvas