#from PIL import Image as im

#image=im.open('Nummer_1.jpg')

#target_color=(255, x, y)

#width, height=im.size

#pixel_count=0

#for a in range(width):
    #for b in range(height):
        #c=im.getpixel((x,y))
        #if <c[x]<

from PIL import Image# Bild laden

image = Image.open('Nummer_1_W2.png')# Farbe angeben (hier: rot)
target_color = [(255,255,0),(255,215,0),(255,247,0),(255,183,0),(255,219,88),(255,225,53),(255,204,51), (0,0,0,0)]# Größe des Bildes bestimmen
width, height = image.size# Anzahl der Pixel im Bild mit der target_color
pixel_count = 0# Schleife durch alle Pixel
for x in range(width):
    for y in range(height):# Farbe des aktuellen Pixels auslesen
        pixel_color = image.getpixel((x, y))# Überprüfen, ob die Farbe mit der target_color übereinstimmt
        for i in range (len(target_color)):
            print(target_color[i], pixel_color)
            if pixel_color==target_color[i]:
                pixel_count += 1

print(f"Das Bild hat {pixel_count} Pixel in der Farbe {target_color}.")





