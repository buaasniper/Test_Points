
from itertools import izip
from PIL import Image
from PIL import ImageChops

im1 = Image.open('result.png')
print list(im1.getdata())
'''
im2 = Image.open('2.png')
diff1 = ImageChops.subtract(im1,im2,0.01,0)
diff2 = ImageChops.subtract(im2,im1,0.01,0)
diff = ImageChops.add(diff1, diff2)
print list(diff.getdata())
diff.show()
diff.save('wsjwsj.png')
pairs = izip(im1.getdata(), im2.getdata())
if len(im1.getbands()) == 1:
    dif = sum(abs(p1 - p2) for p1,p2 in pairs)
else:
    dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))
ncomponents = im1.size[0] * im1.size[1] * 3
print "Difference (percentage):", (dif / 255.0 * 100) / ncomponents'''