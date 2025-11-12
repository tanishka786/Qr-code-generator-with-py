import qrcode
from PIL import Image
import numpy as np
import imageio
import os
import re

# === User Input ===
url = input("Enter the URL you want to generate QR for: ").strip()
file_name = input(
    "Enter the name you want for your QR code (without extension): ").strip()

# === Sanitize file name ===
# Remove or replace invalid characters from file names
file_name = re.sub(r'[\\/*?:"<>|]', "_", file_name)

# === File Path Setup ===
output_dir = r"C:\Users\TANISHKA\Desktop\qr code\qrcode img"
os.makedirs(output_dir, exist_ok=True)
file_path = os.path.join(output_dir, f"{file_name}_rainbow.gif")

# === Generate QR Code ===
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Convert QR to image
base_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
base_array = np.array(base_img)

# === Create Animated Rainbow Frames ===
frames = []
num_frames = 20  # Number of animation frames

for i in range(num_frames):
    frame = base_array.copy()
    h, w, _ = frame.shape

    # Rainbow coloring logic
    for y in range(h):
        for x in range(w):
            if not np.all(frame[y, x] == [255, 255, 255]):  # only color black pixels
                r = int(128 + 127 * np.sin(2 * np.pi * (x / w) + i * 0.3))
                g = int(128 + 127 * np.sin(2 * np.pi * (y / h) + i * 0.5))
                b = int(128 + 127 * np.sin(2 * np.pi *
                        ((x + y) / (w + h)) + i * 0.7))
                frame[y, x] = [r, g, b]

    frames.append(Image.fromarray(frame))

# === Save Animated QR ===
frames[0].save(
    file_path,
    save_all=True,
    append_images=frames[1:],
    duration=100,
    loop=0
)

print(f"🎉 Rainbow QR code successfully generated at:\n{file_path}")
print("Scan it — and shine like a rainbow 🌈✨\nThanks to BRO CODE 😎")
