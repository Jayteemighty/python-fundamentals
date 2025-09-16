import qrcode
import os
from datetime import datetime
from pathlib import Path

def create_qr_code():
    print("QR Code Generator")
    
    data = input("Enter what you would like to encode into QR code: ").strip()
    
    if not data:
        print("No input provided. Exiting.")
        return
    
    # Get custom filename
    default_name = "qrcode"
    custom_name = input(f"Enter filename (default: '{default_name}'): ").strip()
    filename = custom_name if custom_name else default_name
    
    # Ask for save location
    save_path = input("Enter save directory (press Enter for current directory): ").strip()
    if not save_path:
        save_path = os.getcwd()  # Current working directory
    else:
        # Create directory if it doesn't exist
        os.makedirs(save_path, exist_ok=True)
    
    # Customization options
    print("\nCustomization Options:")
    print("1. Default (black on white)")
    print("2. Custom colors")
    print("3. Advanced settings")
    
    choice = input("Choose option (1-3, default: 1): ").strip() or "1"
    
    if choice == "1":
        img = qrcode.make(data)
        final_path = os.path.join(save_path, f"{filename}.png")
        img.save(final_path)
        print(f"QR code saved as: {final_path}")
        
    elif choice == "2":
        fill_color = input("Enter fill color (default: black): ").strip() or "black"
        back_color = input("Enter background color (default: white): ").strip() or "white"
        
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        
        final_path = os.path.join(save_path, f"{filename}_{fill_color}_{back_color}.png")
        img.save(final_path)
        print(f"Colored QR code saved as: {final_path}")
        
    elif choice == "3":
        try:
            version = int(input("QR version (1-40, default: 1): ").strip() or "1")
            box_size = int(input("Box size (default: 10): ").strip() or "10")
            border = int(input("Border size (default: 4): ").strip() or "4")
            fill_color = input("Fill color (default: black): ").strip() or "black"
            back_color = input("Background color (default: white): ").strip() or "white"
            
            qr = qrcode.QRCode(
                version=version,
                box_size=box_size,
                border=border,
                error_correction=qrcode.constants.ERROR_CORRECT_H
            )
            qr.add_data(data)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color=fill_color, back_color=back_color)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            final_path = os.path.join(save_path, f"{filename}_advanced_{timestamp}.png")
            img.save(final_path)
            
            print(f"Advanced QR code saved as: {final_path}")
            print(f"   Settings: Version={version}, Box Size={box_size}, Border={border}")
            
        except ValueError:
            print("Invalid input. Using default settings.")
            img = qrcode.make(data)
            final_path = os.path.join(save_path, f"{filename}.png")
            img.save(final_path)
            print(f"QR code saved as: {final_path}")
    
    else:
        print("Invalid choice. Using default settings.")
        img = qrcode.make(data)
        final_path = os.path.join(save_path, f"{filename}.png")
        img.save(final_path)
        print(f"QR code saved as: {final_path}")
    
    # Preview the file location
    if os.path.exists(final_path):
        file_size = os.path.getsize(final_path) / 1024  # Convert to KB
        print(f"File size: {file_size:.2f} KB")
        print(f"Full path: {final_path}")
    else:
        print("Error: File was not created successfully.")

def main():
    while True:
        create_qr_code()
        
        # Ask if user wants to create another QR code
        another = input("\nCreate another QR code? (y/n): ").lower().strip()
        if another not in ['y', 'yes']:
            print("Thank you for using QR Code Generator!")
            break
        print()

if __name__ == "__main__":
    main()