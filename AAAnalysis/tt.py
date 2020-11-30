from tkinter import *
from PIL import Image
from PIL import ImageTk

window = Tk()
window.title('My Window')
window.geometry('600x800')

# 在图形界面上创建 500 *500 大小的画布
canvas = Canvas(window, bg='green', height=500, width=500)
canvas.pack()

# 说明图片位置，并导入图片到画布上
im1 = None
im2 = None
im1 = Image.open("first.jpg")  # 支持相对或绝对路径，支持多种格式
im2 = ImageTk.PhotoImage(im1)
canvas.create_image(10, 10, anchor=NW, image=im2)

window.mainloop()