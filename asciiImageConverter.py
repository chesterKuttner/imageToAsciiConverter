from PIL import Image
# import matplotlib.pyplot as plt
import numpy as np
#matploplib inline
from math import floor

img= Image.open('image.jpg')
# height=int(input('GIVE ME HEIGHT... please:'))
# width=int(input('and width UwU:'))
height=100
width=100
rez=(height,width)
img=img.resize(rez)
img=img.convert('LA')
# img.show()
grid=[]

chars=[' ','.',',','-',':','+','=','/','(',')','#','6','Q']

for y in range(1,height):
    row=[]
    for x in range(1,width):
        rgb= img.getpixel((x,y))
        row.append(rgb[0]+rgb[1])
    grid.append(row)

chosenCombinations=[]
for element in grid:
    for e in element:
        if e not in chosenCombinations:
            chosenCombinations.append(e)
chosenCombinations.sort()

darkest=chosenCombinations[len(chosenCombinations)-1]
lightest=chosenCombinations[0]

interval=(darkest-lightest)/(len(chars)-1)
charGrid=[]
for element in grid:
    charRow=''
    for e in element:
        index=floor((e-lightest)/interval)
        charRow=charRow+(chars[index])
    charGrid.append(charRow)

for element in charGrid:
    print(*element)
        