# http://www.pythonchallenge.com/pc/return/5808.html
# <title>odd even</title>
from PIL import Image

im = Image.open("11_img.jpg")
(w, h) = im.size

even = Image.new("RGB", (w // 2, h // 2))
odd = Image.new("RGB", (w // 2, h // 2))

for i in range(w):
    for j in range(h):
        p = im.getpixel((i, j))
        if (i + j) % 2 == 1:
            odd.putpixel((i // 2, j // 2), p)
        else:
            even.putpixel((i // 2, j // 2), p)

even.save("11_even.jpg")
odd.save("11_odd.jpg")
# key -> evil

