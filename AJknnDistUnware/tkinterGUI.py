from tkinter import *


def init_tkinter():
    tk = Tk()
    tk.title('AJ')
    tk.wm_attributes("-topmost", 1)
    Width = 600
    Height = 600
    canvas = Canvas(tk, width=Width, height=Height, bg='white', highlightthickness=0)
    canvas.pack()
    # canvas.create_line(0, 0, 600, 0)
    # canvas.create_line(150, 0, 150, 150, 0, 150, 150, 150)
    canvas.create_line(Height - 150, Height - 150, Height - 150, Height, Height - 150, Height - 150, Height, Height - 150)
    canvas.pack()
    tk.update()
    return tk, canvas