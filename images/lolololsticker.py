# -*- coding: utf-8 -*-
from PIL import Image
import math
'''
emojilmao=[
    [(255, 0, 0),'❤️'],
    [(255,165,0),'🧡'],
    [(255,255,0),'💛'],
    [(0,255,0),'💚'],
    [(0,0,255),'💙'],
    [(230,230,250),'💜'],
    [(165,42,42),'🤎'],
    [(0,0,0),'🖤'],
    [(255,255,255),'🤍']              
         ]
'''

emojilmao={
    (255, 0, 0):'❤️',
    (255,165,0):'🧡',
    (255,255,0):'💛',
    (0,255,0):'💚',
    (0,0,255):'💙',
    (230,230,250):'💜',
    (165,42,42):'🤎',
    (0,0,0):'🖤',
    (255,255,255):'🤍',
    (259,216,203):'🍑'            
         }

def findclosecolor(p):
    s=195076
    pixels=[0,0,0]
    for i in emojilmao.keys():
        a=i[0]-p[0]
        b=i[1]-p[1]
        c=i[2]-p[2]
        distance=math.sqrt(a*a+b*b+c*c)
        if(distance<s):
            s=distance
            pixels=(a+p[0],b+p[1],c+p[2])
    return pixels
   
# Create an image as input:
'''
input_image = Image.new(mode="RGB", size=(400, 400),
                        color="blue")
  
# save the image as "input.png"
#(not mandatory)
input_image.save("input", format="png")
'''
input_image = Image.open('C:/Users/jadej/OneDrive/Pictures/lowrespika.png')   
input_image = Image.open('C:/pythonlove/wonderla12.jpg')   
input_image = Image.open('C:/pythonlove/wepika.jpg')   
# Extracting pixel map:
pixel_map = input_image.load()
print(type(pixel_map))
# Extracting the width and height
# of the image:
print(type(input_image.size))
print(findclosecolor([244,244,244]))
width, height = input_image.size
z = 100

fs=open('C:/pythonlove/test.txt','w', encoding="utf-8")


for i in range(height):
    for j in range(width):
        fs.write(emojilmao[findclosecolor(pixel_map[j,i])])
    fs.write('\n')
fs.close()
'''
for i in range(width):
    for j in range(height):
        
        # the following if part will create
        # a square with color orange
        if((i >= z and i <= width-z) and (j >= z and j <= height-z)):
            
            # RGB value of orange.
            pixel_map[i, j] = (255, 165, 0)
  
        # the following else part will fill the
        # rest part with color light salmon.
        else:
            
            # RGB value of light salmon.
            pixel_map[i, j] = (255, 160, 122)
'''
# The following loop will create a cross
# of color blue.
'''
for i in range(width):
    
    # RGB value of Blue.
    pixel_map[i, i] = (0, 0, 255)
    pixel_map[i, width-i-1] = (0, 0, 255)
'''
# Saving the final output
# as "output.png":
'''
input_image.save("output", format="png")
input_image.show()
print('How to print 😁😛😋🤣emojis using python🐍')
gen=Image.new()
'''
# use input_image.show() to see the image on the
# output screen.