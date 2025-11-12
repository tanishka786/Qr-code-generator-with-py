import qrcode
import os
import re

# url whose QR you want to generate
url = input("Enter the URL: ").strip()

# ask user what to name the QR code (optional)
file_name = input(
    "Enter the name for your QR code file (without extension): ").strip()
# sanitize + fallback
file_name = re.sub(r'[\\/*?:"<>|]', "_", file_name) or "qrcode"

# where you want to store the generated qr codes
file_path = f"C:\\Users\\TANISHKA\\Desktop\\qr code\\qrcode img\\{file_name}.png"
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# generating qr code python object
qr = qrcode.QRCode()

# adding data to qrcode obj
qr.add_data(url)

# to generate the qr image
img = qr.make_image()

# store to the file path that we mentioned above
img.save(file_path)

print("Congratulations! your QR code is generated successfully! 🎉")
print(f"Saved at: {file_path}")
print("Thanks to BRO CODE 😎")
