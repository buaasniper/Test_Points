from PIL import Image
n = 256
im = Image.new("RGBA", (n, n))
pix = im.load()
for x in range(n):
    for y in range(n):
        pix[x,y] = (x, x, x, y)
im.save("testtest.png", "PNG")
im.show()
im = Image.open('testtest.png')
print list(im.getdata())