import image as img
import math

# CREATE AN IMAGE FROM A FILE
image = img.image("arch.jpg")

# LOOP THROUGH ALL THE PIXELS
pixels = img.getPixels()
for i, p in enumerate(pixels):

    # CLEAR THE RED
    p.setRed(math.sin(i//2)*255)
    p.setGreen(math.cos(i)*255)
    img.updatePixel(p)

# SHOW THE CHANGED IMAGE
win = img.ImageWin(img.getWidth(),img.getHeight())
img.draw(win)