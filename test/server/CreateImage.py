from PIL import Image

im = Image.new("RGB", (256, 256))
pix = im.load()
for x in range(256):
    for y in range(256):
        pix[x,y] = (34,30,31)
im.save("testtest.png", "PNG")
im.show()
im = Image.open('testtest.png')
print list(im.getdata())