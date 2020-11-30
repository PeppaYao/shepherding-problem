from tkinter import *
from PIL import Image, ImageDraw
from PIL import ImageFont

from PIL import ImageGrab

width = 400
height = 300
center = height // 2
white = (222, 222, 220)
green = (0, 128, 0)
red = (128, 0, 0)

root = Tk()
canvas = Canvas(root, width=width, height=height, bg='white')
step = 1
step_txt = canvas.create_text(120, 20, text="steps: {}/2000".format(step), font=("宋体", 18))
canvas.pack()
# image1 = Image.new("RGB", (width, height), white)
# draw = ImageDraw.Draw(image1)
# cv.create_line([0, center, width, center], fill='green')
# draw.line([0, center, width, center], green)
# draw.line([0, 100, width, 100], red)
# font = ImageFont.truetype("consola.ttf", 40, encoding="unic"  )  # 设置字体
# font = ImageFont.truetype("C:\Windows\Fonts\simfang.ttf", 40, encoding="utf-8")
# draw.text((0, 50), "xxx", 'fuchsia', font)


ImageGrab.grab().crop(white, height).save("first.pdf")
#
# filename = "third.pdf"
# image1.save(filename)
root.mainloop()