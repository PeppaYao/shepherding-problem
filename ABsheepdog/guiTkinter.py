from tkinter import *

tk = Tk()
tk.title('ADshepherd_raw')
tk.wm_attributes("-topmost", 1)
Width = 600
Height = 600
canvas = Canvas(tk, width=Width, height=Height, bg='white', highlightthickness=0)
canvas.pack()
canvas.create_line(Width / 2, 0, Width / 2, Height)
canvas.create_line(0, Height / 2, Height, Height / 2)
canvas.create_line(Height - 150, Height - 150, Height - 150, Height, Height - 150, Height - 150, Height, Height - 150)
tk.update()
colors = ['green', 'blue', 'blue', 'green']

all_sheep = [[150, 300], [310, 130], [90, 250], [20, 110], [400, 410]]
canvas.create_polygon(50, 100, 100, 100, 80, 80, fill=colors[1])
# for sheep in all_sheep:
#     canvas.create_polygon(sheep[0], sheep[1], sheep[0] + 10, sheep[1] + 10, 100, 100, fill=colors[1])


tk.mainloop()
