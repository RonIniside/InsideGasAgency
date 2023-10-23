import qrcode

img = qrcode.make("https://pypi.org/project/qrcode/")
img.save("qrcodee.jpg")