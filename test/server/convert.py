try:
    import Image
except ImportError:
    from PIL import Image

im1 = Image.open('test.png')
im1 = im1.convert('RGB')
im1.save('result.png')