import sys
import os
from PIL import Image, ImageOps

def main():
    # Ensure exactly two command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 3 else "Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check file extensions
    valid_extensions = (".jpg", ".jpeg", ".png")
    if not input_file.lower().endswith(valid_extensions) or not output_file.lower().endswith(valid_extensions):
        sys.exit("Invalid input or output format")
    
    # Ensure input and output have the same extension
    if os.path.splitext(input_file)[1].lower() != os.path.splitext(output_file)[1].lower():
        sys.exit("Input and output have different extensions")

    # Check if the input file exists
    if not os.path.exists(input_file):
        sys.exit("Input does not exist")

    # Load shirt.png
    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("shirt.png not found")

    # Open the input image
    try:
        image = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # Resize and crop the input image to match the size of the shirt
    image = ImageOps.fit(image, shirt.size)

    # Overlay the shirt onto the image
    image.paste(shirt, shirt)

    # Save the result
    image.save(output_file)

if __name__ == "__main__":
    main()
