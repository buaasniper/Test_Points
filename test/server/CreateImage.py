from PIL import Image
n = 256
im = Image.new("RGBA", (n, n))
pix = im.load()
for x in range(n):
    for y in range(n):
        '''
        if (x + y) % 2 == 0:
            pix[x,y] = (127, 127, 127, 255)
        else:
            pix[x,y] = (128,128,128,255)'''
        pix[x, y] = (129, 129, 129, 255)
im.save("RGBA.png", "PNG")
im.show()
im = Image.open('RGBA.png')
print list(im.getdata())