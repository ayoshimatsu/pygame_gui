import tkinter
from PIL import Image

width = 336
height = 240
map_data = [
    [0, 1, 0, 2, 2, 2, 2],
    [3, 0, 0, 0, 2, 2, 2],
    [3, 0, 0, 1, 0, 0, 0],
    [3, 3, 0, 0, 0, 0, 1],
    [3, 3, 3, 3, 0, 0, 0]
]

img = Image.open("../picture/chip0.png")
print(img.size)

root = tkinter.Tk()
root.title("マップデータ")
canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()
img = [
    tkinter.PhotoImage(file="../picture/chip0.png"),
    tkinter.PhotoImage(file="../picture/chip1.png"),
    tkinter.PhotoImage(file="../picture/chip2.png"),
    tkinter.PhotoImage(file="../picture/chip3.png")
]

for y in range(5):
    for x in range(7):
        n = map_data[y][x]
        canvas.create_image(x * (width/7) + (width/14), y * (height/5) + (height/10), image=img[n])

root.mainloop()
