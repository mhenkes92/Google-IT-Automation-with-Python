
#!/usr/bin/env python3

from PIL import Image
import os

# Specify the input and output folder paths (expanded from tilde)
input_folder = os.path.expanduser("~/supplier-data/images")
output_folder = os.path.expanduser("~/supplier-data/images")

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List all files in the input folder
files = os.listdir(input_folder)

# Loop through each file in the folder
for image in files:
    # Check if the file is a TIFF image
    if image.lower().endswith((".tiff", ".tif")):
        # Create the full path to the input image
        input_image_path = os.path.join(input_folder, image)

        # Open the image using Pillow and ensure it's closed properly
        with Image.open(input_image_path) as img:
            # Convert RGBA to RGB
            img = img.convert("RGB")

            # Resize the image to 600x400
            img = img.resize((600, 400))

            # Construct the output image path by changing the extension to JPEG
            output_image_path = os.path.join(output_folder, os.path.splitext(image)[0] + ".jpeg")

            # Save the resized and converted image as JPEG
            img.save(output_image_path, "JPEG")

print("Conversion complete.")

