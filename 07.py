# http://www.pythonchallenge.com/pc/def/oxygen.html
# image has a gray scale
# <title>smarty</title>
# smarty is a library in python
from PIL import Image
import re

img = Image.open("07_img.png")
# get the gray scale
row = [img.getpixel((x, img.height / 2)) for x in range(img.width)]
row = row[::7]  # each gray is 7 pixles
# at the right end not all is gray, delete the noise
ords = [r for r, g, b, a in row if r == g == b]
# ASCII char
print("".join(map(chr, ords)))
# [105, 110, 116, 101, 103, 114, 105, 116, 121]

char = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print("".join(map(chr, map(int, char))))
# key = integrity
