import qrcode

data = "My name is JT."
img = qrcode.make(data)

img.save('C:/Users/JAYTEE/Pictures/qrcode.png')

# For editing how the qr code appear
qr = qrcode.QRCode(version = 1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color = 'red', back_color = 'white')
img.save('C:/Users/JAYTEE/Pictures/qrcode2.png')
