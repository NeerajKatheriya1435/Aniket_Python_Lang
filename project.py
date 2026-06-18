import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(input("Enter the text you want QR: "))
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="red")
img.save("newFile.png")  