from PIL import Image
n = 512
im = Image.new("RGB", (n, n))
pix = im.load()
for x in range(n):
    for y in range(n):
        pix[x,y] = (34,30,31)
im.save("testtest.png", "PNG")
im.show()
im = Image.open('testtest.png')
print list(im.getdata())