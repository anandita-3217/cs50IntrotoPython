import sys
import os
from PIL import Image, ImageOps

def try_shirt(input_file,output_file):
    shirt = Image.open("shirt.png")

    image = Image.open(input_file)
    image = ImageOps.fit(image,shirt.size)
    image.paste(shirt,shirt)
    image.save(output_file)


def main():
    
    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 3 else "Too many command-line arguments") 
    input_file =sys.argv[1]
    output_file =sys.argv[2]
    validextensions = (".jpg",".jpeg",".png")
    if not input_file.lower().endswith(validextensions) or not output_file.lower().endswith(validextensions):
        sys.exit("Invalid input")
    if not os.path.exists(input_file):
        sys.exit("File not found")
    if os.path.splitext(input_file)[1].lower() != os.path.splitext(output_file)[1].lower():
        sys.exit("Input and output have different extensions")
    try_shirt(input_file,output_file)
        
if __name__ == "__main__":
    main()