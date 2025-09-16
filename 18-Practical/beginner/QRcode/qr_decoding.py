import cv2
import os

def decode_qr_code(image_path):
    try:
        # Check if file exists
        if not os.path.exists(image_path):
            print(f"Error: File '{image_path}' not found.")
            return None
        
        # Read the image
        img = cv2.imread(image_path)
        
        if img is None:
            print(f"Error: Could not read image from '{image_path}'")
            return None
        
        # Initialize QR code detector
        detector = cv2.QRCodeDetector()
        
        # Detect and decode QR code
        data, vertices_array, binary_qrcode = detector.detectAndDecode(img)
        
        if vertices_array is not None:
            print("QR Code successfully decoded!")
            print(f"Data: {data}")
            
            # Optional: Draw bounding box around QR code (for visualization)
            if len(vertices_array) > 0:
                print(f"QR code position detected in image")
            
            return data
        else:
            print("No QR code found in the image.")
            return None
            
    except Exception as e:
        print(f"Error decoding QR code: {e}")
        return None

if __name__ == "__main__":
    # Specify the path to your QR code image
    image_path = 'C:/Users/JAYTEE/Pictures/qrcode.png'
    
    # Alternative: Ask user for image path
    # image_path = input("Enter the path to your QR code image: ").strip()
    
    print("QR Code Decoder")
    print("=" * 30)
    
    result = decode_qr_code(image_path)
    
    if result:
        print(f"\n Decoding successful!")
    else:
        print(f"\n Could not decode QR code.")