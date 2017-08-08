try:
    import Image
except ImportError:
    from PIL import Image

im1 = Image.open('RGBA.png')
im1 = im1.convert('RGB')
im1.save('RGB.png')
print list(im1.getdata())