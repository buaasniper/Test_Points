'''from binascii import a2b_base64
def index(req):
    postData = req.form
    json = str(postData['param'].value)
    data = 'MY BASE64-ENCODED STRING'
binary_data = a2b_base64(data)
fd = open('image.png', 'wb')
fd.write(json)
fd.close()'''