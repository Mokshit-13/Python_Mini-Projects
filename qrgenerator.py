import qrcode

text_message = "HI!, I JUST STARTED DOING MINI PROJECTS..."
qr = qrcode.QRCode()
qr.add_data(text_message)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("QR.png")

print("Success, saved as image")