from PIL import Image
import numpy as np
from math import floor

img = Image.open('image.jpg')
height = img.height
width = img.width

#not my code https://github.com/python/cpython/blob/3.9/Lib/colorsys.py
def rgb_to_hls(r, g, b):
    maxc = max(r, g, b)
    minc = min(r, g, b)
    # XXX Can optimize (maxc+minc) and (maxc-minc)
    l = (minc+maxc)/2.0
    if minc == maxc:
        return 0.0, l, 0.0
    if l <= 0.5:
        s = (maxc-minc) / (maxc+minc)
    else:
        s = (maxc-minc) / (2.0-maxc-minc)
    rc = (maxc-r) / (maxc-minc)
    gc = (maxc-g) / (maxc-minc)
    bc = (maxc-b) / (maxc-minc)
    if r == maxc:
        h = bc-gc
    elif g == maxc:
        h = 2.0+rc-bc
    else:
        h = 4.0+gc-rc
    h = (h/6.0) % 1.0
    return h, l, s
#not my code https://github.com/python/cpython/blob/3.9/Lib/colorsys.py
def rgb_to_hsv(r, g, b):
    maxc = max(r, g, b)
    minc = min(r, g, b)
    v = maxc
    if minc == maxc:
        return 0.0, 0.0, v
    s = (maxc-minc) / maxc
    rc = (maxc-r) / (maxc-minc)
    gc = (maxc-g) / (maxc-minc)
    bc = (maxc-b) / (maxc-minc)
    if r == maxc:
        h = bc-gc
    elif g == maxc:
        h = 2.0+rc-bc
    else:
        h = 4.0+gc-rc
    h = (h/6.0) % 1.0
    return h, s, v


def colourInRange(colour1, colour2, range):
    c1=rgb_to_hls(*colour1)
    c2=rgb_to_hls(*colour2)

    if ((c2[0]-range) < c1[0] < (c2[0]+range)) and ((c2[1]-range) < c1[1] < (c2[1]+range)) and ((c2[2]-range) < c1[2] < (c2[2]+range)):
        return True
    else:
        return False


grid = []
for y in range(0, height):
    for x in range(0, width):
        rgb = img.getpixel((x, y))
        grid.append([(x, y), rgb])

# print(grid)
allColours = [(139, 0, 0),
              (165, 42, 42),
              (178, 34, 34),
              (220, 20, 60),
              (255, 0, 0),
              (255, 99, 71),
              (255, 127, 80),
              (205, 92, 92),
              (240, 128, 128),
              (233, 150, 122),
              (250, 128, 114),
              (255, 160, 122),
              (255, 69, 0),
              (255, 140, 0),
              (255, 165, 0),
              (255, 215, 0),
              (184, 134, 11),
              (218, 165, 32),
              (238, 232, 170),
              (189, 183, 107),
              (240, 230, 140),
              (128, 128, 0),
              (255, 255, 0),
              (154, 205, 50),
              (85, 107, 47),
              (107, 142, 35),
              (124, 252, 0),
              (127, 255, 0),
              (173, 255, 47),
              (0, 1, 0),
              (0, 128, 0),
              (34, 139, 34),
              (0, 255, 0),
              (50, 205, 50),
              (144, 238, 144),
              (152, 251, 152),
              (143, 188, 143),
              (0, 250, 154),
              (0, 255, 127),
              (46, 139, 87),
              (102, 205, 170),
              (60, 179, 113),
              (32, 178, 170),
              (47, 79, 79),
              (0, 128, 128),
              (0, 139, 139),
              (0, 255, 255),
              (0, 255, 255),
              (224, 255, 255),
              (0, 206, 209),
              (64, 224, 208),
              (72, 209, 204),
              (175, 238, 238),
              (127, 255, 212),
              (176, 224, 230),
              (95, 158, 160),
              (70, 130, 180),
              (1, 149, 237),
              (0, 191, 255),
              (30, 144, 255),
              (173, 216, 230),
              (135, 206, 235),
              (135, 206, 250),
              (25, 25, 112),
              (0, 0, 128),
              (0, 0, 139),
              (0, 0, 205),
              (0, 0, 255),
              (65, 105, 225),
              (138, 43, 226),
              (75, 0, 130),
              (72, 61, 139),
              (106, 90, 205),
              (123, 104, 238),
              (147, 112, 219),
              (139, 0, 139),
              (148, 0, 211),
              (153, 50, 204),
              (186, 85, 211),
              (128, 0, 128),
              (216, 191, 216),
              (221, 160, 221),
              (238, 130, 238),
              (255, 0, 255),
              (218, 112, 214),
              (199, 21, 133),
              (219, 112, 147),
              (255, 20, 147),
              (255, 105, 180),
              (255, 182, 193),
              (255, 192, 203),
              (250, 235, 215),
              (245, 245, 220),
              (255, 228, 196),
              (255, 235, 205),
              (245, 222, 179),
              (255, 248, 220),
              (255, 250, 205),
              (250, 250, 210),
              (255, 255, 224),
              (139, 69, 19),
              (160, 82, 45),
              (210, 105, 30),
              (205, 133, 63),
              (244, 164, 96),
              (222, 184, 135),
              (210, 180, 140),
              (188, 143, 143),
              (255, 228, 181),
              (255, 222, 173),
              (255, 218, 185),
              (255, 228, 225),
              (255, 240, 245),
              (250, 240, 230),
              (253, 245, 230),
              (255, 239, 213),
              (255, 245, 238),
              (245, 255, 250),
              (112, 128, 144),
              (119, 136, 153),
              (176, 196, 222),
              (230, 230, 250),
              (255, 250, 240),
              (240, 248, 255),
              (248, 248, 255),
              (240, 255, 240),
              (255, 255, 240),
              (240, 255, 255),
              (255, 250, 250),
              (0, 0, 0),
              (105, 105, 105),
              (128, 128, 128),
              (169, 169, 169),
              (192, 192, 192),
              (211, 211, 211),
              (220, 220, 220),
              (245, 245, 245),
              (255, 255, 255)]
coreColours = []
r = 1.5

for i in range(0, floor(len(allColours)/r)):
    coreColours.append(allColours[round(i*r)])


iTop = len(coreColours)
print(iTop)
i = 0
show = 0
for coreColour in coreColours:
    i += 1
    if round(i/iTop*10) > round(show/10):
        show = round(i/iTop*100)
        print(show,'%')
    for imgColour in grid:
        if colourInRange(coreColour, imgColour[1], 2*r):
            img.putpixel(imgColour[0], coreColour)
            grid.pop(grid.index(imgColour))
    if len(grid) == 0:
        break

img.show()
