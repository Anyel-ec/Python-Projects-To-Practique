import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Decode a QR code from an image
def decode_qr_code(image_path):
    # Open the image containing the QR code
    img = Image.open(image_path)

    # Decode the QR code
    decoded_objects = decode(img)

    if decoded_objects:
        # Display the decoded information
        for obj in decoded_objects:
            print(f"Type: {obj.type}")
            print(f"Content: {obj.data.decode('utf-8')}")

# Call the function with the path to the QR code image
decode_qr_code('image_path.png')
