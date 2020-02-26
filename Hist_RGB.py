import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw 

image = Image.open("C:\\Users\\Pivnica\\Desktop\\lena.png") # открыть по пути 
width = image.size[0] # считать колличество строк
height = image.size[1] # считать колличество столбцов
pix = image.load() # считать пиксели

red = [] 
green = [] 
blue = []
sr = []

# разбить каждый пиксель на цвета
for i in range(width):
    for j in range(height):
        red.append(pix[i, j][0])
        green.append(pix[i, j][1])
        blue.append(pix[i, j][2])
        sr.append((pix[i, j][0] + pix[i, j][1] + pix[i, j][2]) // 3)

fig = plt.figure() # создание
ax = fig.add_subplot(2, 1, 1) # 2 строки, 1 столбик, ?

#t = np.arange(0.0, 1.0, 0.01) # ?, длина, скругление
#s = np.sin(2*np.pi*t)
#line = ax.plot(t, s, color='blue', lw=2)
#line1 = ax.plot(t, -s, color='red', lw=2)
ytext = ax.set_ylabel('Контраст') # текст прямой по Y
xtext = ax.set_xlabel('Кол-во') # текст прямой по X

#np.random.seed(19680801)

#ax2 = fig.add_subplot(2, 1, 1) # 2 строки, 1 столбик, ?
#n, bins, patches = ax.hist(red, 200, facecolor='red', edgecolor='red')
#n, bins, patches = ax.hist(green, 200, facecolor='green', edgecolor='green')
#n, bins, patches = ax.hist(blue, 10, facecolor='blue', edgecolor='blue')
n, bins, patches = ax.hist(sr, 200, facecolor='black', edgecolor='black')
''' ax2.hist - данные, масштаб?, цвет столбиков, цвет контура'''













