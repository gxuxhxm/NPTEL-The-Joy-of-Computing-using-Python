from PIL import Image
import numpy as np
import random

im = Image.open('map01.png')
RGB_im = im.convert('RGB')

count_Punjab = 0
count_India = 0
count = 0

while count <= 100000:
    x = random.randint(0, 2480)
    y = random.randint(0, 2735)
    z = 0

    r, g, b = RGB_im.getpixel((x, y))

    if r == 60:
        count_India += 1
    elif r == 80:
        count_Punjab += 1
    count += 1

area_Punjab = (count_Punjab / count_India) * 3287263
print("Area of Punjab:", area_Punjab)