from pyzbar.pyzbar import decode
from PIL import Image
import os

def decode_qr_code(image_path):
    try:
        # Check if file exists
        if not os.path.exists(image_path):
            print(f"Error: File '{image_path}' not found.")
            return None
        
        # Open and decode the image
        img = Image.open(image_path)
        result = decode(img)
        
        # Process the results
        if result:
            print("QR Code(s) detected:")
            for i, decoded_data in enumerate(result):
                print(f"QR Code {i+1}:")
                print(f"  Data: {decoded_data.data.decode('utf-8')}")
                print(f"  Type: {decoded_data.type}")
                print(f"  Quality: {len(decoded_data.polygon)} points detected")
        else:
            print("No QR codes found in the image.")
            return None
            
        return result
        
    except Exception as e:
        print(f"Error decoding QR code: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # You can change this path to your QR code image
    image_path = 'C:/Users/JAYTEE/Pictures/qrcode.png'
    
    # Alternative: ask user for image path
    # image_path = input("Enter the path to your QR code image: ")
    
    result = decode_qr_code(image_path)